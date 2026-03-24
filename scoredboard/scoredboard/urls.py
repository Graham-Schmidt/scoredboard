"""
URL configuration for scoredboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import display_board, home, create_game, control_board

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO homepage
    path('game/create/',  create_game),
    path('game/<str:code>/display/', display_board, name="game_display"),
    path('game/<str:code>/control/', control_board, name="game_control"),
]
