from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def display_board(request):
    template = loader.get_template("display.html")
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))