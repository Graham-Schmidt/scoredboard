import random
import string
from datetime import timezone, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .forms import CreateGameForm

def generate_code():
    """Generate a unique 6-digit code"""
    return ''.join(random.choices(string.digits, k=6))

def display_board(request):
    template = loader.get_template("display.html")
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

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