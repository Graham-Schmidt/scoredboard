import base64
import io
import random
import string
from datetime import timedelta

import qrcode
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .forms import CreateGameForm
from .models import Game
from .sports import SPORTS, SPORTS_BY_SLUG


def generate_code():
    """Generate a unique 6-digit code"""
    return "".join(random.choices(string.digits, k=6))


def is_expired(game):
    return not game.is_active or game.expires_at < timezone.now()


# VIEWS
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))


def display_board(request, code):
    game = Game.objects.get(code=code)
    if is_expired(game):
        return render(request, "expired.html")
    template = loader.get_template("display.html")
    return HttpResponse(template.render({"code": code, "game": game}, request))


def control_board(request, code):
    game = Game.objects.get(code=code)
    if is_expired(game):
        return render(request, "expired.html")
    sport_key = f"sport_{code}"

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "set_sport":
            request.session[sport_key] = request.POST.get("sport")

        elif action == "update":
            try:
                game.team_a_score = int(request.POST["team_a_score"])
                game.team_b_score = int(request.POST["team_b_score"])
                game.save()
                async_to_sync(get_channel_layer().group_send)(
                    f"game_{code}",
                    {
                        "type": "score_update",
                        "team_a_score": game.team_a_score,
                        "team_b_score": game.team_b_score,
                    },
                )
            except (KeyError, ValueError):
                pass

        return redirect("game_control", code=code)

    sport_slug = request.session.get(sport_key)
    sport = SPORTS_BY_SLUG.get(sport_slug)

    return render(
        request,
        "control.html",
        {
            "code": code,
            "game": game,
            "sports": SPORTS,
            "sport": sport,
        },
    )


def game_score(request, code):
    game = Game.objects.get(code=code)
    if is_expired(game):
        return JsonResponse({"error": "expired"}, status=410)
    return JsonResponse(
        {"team_a_score": game.team_a_score, "team_b_score": game.team_b_score}
    )


def game_created(request, code):
    game = Game.objects.get(code=code)
    control_url = request.build_absolute_uri(reverse("game_control", args=[code]))
    img = qrcode.make(control_url)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_data_uri = (
        "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()
    )
    return render(request, "game-created.html", {"game": game, "qr_code": qr_data_uri})


def create_game(request):
    if request.method == "POST":
        form = CreateGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.code = generate_code()
            game.expires_at = timezone.now() + timedelta(hours=4)
            game.save()
            return redirect("game_created", code=game.code)
    else:
        form = CreateGameForm()

    return render(request, "create-game.html", {"form": form})
