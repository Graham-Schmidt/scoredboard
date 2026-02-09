from datetime import datetime

from django.db import models

class Game(models.Model):
    name: str
    team_a_name: str
    team_b_name: str
    team_a_score: int
    team_b_score: int
    game_cdoe: str
    expiration_datetime: datetime

    