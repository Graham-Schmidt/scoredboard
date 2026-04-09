from datetime import datetime

from django.db import models


class Game(models.Model):
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    team_a_name = models.CharField(max_length=100)
    team_b_name = models.CharField(max_length=100)
    team_a_score = models.IntegerField(default=0)
    team_b_score = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.team_a_name} vs {self.team_b_name} ({self.code})"
