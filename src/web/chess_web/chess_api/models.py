from django.db import models

# Create your models here.

class ChessUser(models.Model):
    user_id = models.CharField(max_length=12, primary_key=True)
    username = models.CharField(max_length=16)
    game_code = models.CharField(max_length=6)
    color = models.CharField(max_length=30)
