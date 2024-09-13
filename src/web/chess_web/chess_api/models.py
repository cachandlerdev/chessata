from django.db import models

# Create your models here.

class ChessUser(models.Model):
    user_id = models.TextField(max_length=16, primary_key=True)
    username = models.TextField(max_length=16)
    game_code = models.ForeignKey('GameLobby', on_delete=models.CASCADE, related_name="users")
    color = models.TextField(max_length=30)
    
    def __str__(self):
        return f"{self.user_id}: {self.username} ({self.game_code}, {self.color})"


class GameLobby(models.Model):
    game_code = models.TextField(max_length=6, primary_key=True)
    is_over = models.BooleanField(default=False)
    has_started = models.BooleanField(default=False)
    is_white_turn = models.BooleanField(default=True)
    # Match details for reconstructing the game between moves
    board = models.JSONField()
    allow_en_passant = models.JSONField()
    has_king_moved = models.JSONField()
    has_rook_moved = models.JSONField()
    match_state = models.TextField(max_length=30, default="not over")

    def __str__(self):
        return f"{self.game_code}: {self.board} ({self.is_over}, {self.match_state}, {self.is_white_turn}))"
