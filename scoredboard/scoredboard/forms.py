from django import forms

from .models import Game

class CreateGameForm(forms.ModelForm):
   class Meta:
        model = Game
        fields = ['team_a_name', 'team_b_name']
        widgets = {
            'team_a_name': forms.TextInput(attrs={'placeholder': 'Team A'}),
            'team_b_name': forms.TextInput(attrs={'placeholder': 'Team B'}),
        } 
