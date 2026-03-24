import random
import string
from datetime import timezone, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .forms import CreateGameForm, ControlBoardForm
from .models import Game

def generate_code():
    """Generate a unique 6-digit code"""
    return ''.join(random.choices(string.digits, k=6))


# VIEWS
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def display_board(request, code):
    template = loader.get_template("display.html")
    game = Game.objects.get(code=code)
    return HttpResponse(template.render({"code": code, "game": game}, request))

def control_board(request, code):
    game = Game.objects.get(code=code)
    if request.method == 'POST':
        form = ControlBoardForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_control', code=code)
    else:
        form = ControlBoardForm(instance=game)
    
    return render(request, 'control.html', {'form': form, 'code': code})

def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.code = generate_code()
            game.expires_at = timezone.now() + timedelta(hours=4)
            game.save()
            return redirect('game_display', code=game.code)
    else:
        form = CreateGameForm()
    
    return render(request, 'home.html', {'form': form})