from django import forms

from .models import Game, BoardControl

class CreateGameForm(forms.ModelForm):
   class Meta:
        model = Game
        fields = ['team_a_name', 'team_b_name']
        widgets = {
            'team_a_name': forms.TextInput(attrs={'placeholder': 'Team A'}),
            'team_b_name': forms.TextInput(attrs={'placeholder': 'Team B'}),
        } 

class ControlBoardForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['team_a_score', 'team_b_score']
        widgets = {
            'team_a_score': forms.NumberInput(attrs={'placeholder': '0'}),
            'team_b_score': forms.NumberInput(attrs={'placeholder': '0'}),
        }