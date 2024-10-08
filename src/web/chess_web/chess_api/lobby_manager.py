import secrets

from . import models
from . import chess_manager


def create_user(game_code, username):
    """Creates a user for the match with the specified game code and username,
    and returns the user ID and game role (player/spectator). Returns empty 
    strings if the user couldn't be created."""
    if game_code == "" or username == "":
        return "", ""
    
    user_id_length = 12
    user_id = secrets.token_urlsafe(user_id_length)
    
    # Variable doesn't seem to always be respected by secrets.token_urlsafe
    user_id = user_id[:user_id_length]

    if not chess_manager.does_match_exist(game_code):
        chess_manager.create_new_match(game_code)
    role = _get_next_user_role(game_code)

    return user_id, role


def add_user_to_match(user_id, game_code, username):
    """Adds this user to the ChessUser database. We return his color (a 
    spectator's color is the empty string).
    Throws an `IntegrityError` if the user couldn't be saved."""
    other_users = models.ChessUser.objects.filter(game_code=game_code)
    num_of_other_players = len(other_users.exclude(color="").all())
    
    # TODO: Add an option to select the player color
    if num_of_other_players == 0:
        color = "white"
    elif num_of_other_players == 1:
        color = "black"
    else:
        color = ""
    # Save to database
    game = models.GameLobby.objects.get(pk=game_code)
    chess_user = models.ChessUser(user_id=user_id, 
                                username=username,
                                game_code=game,
                                color=color)
    chess_user.save()
    
    return color


def get_other_player(user_id, game_code):
    """Gets the other player in this match."""
    users = models.ChessUser.objects.filter(game_code=game_code)
    players = users.exclude(color="").all()
    other_player = players.exclude(pk=user_id).first()
    return other_player


def _get_next_user_role(game_code):
    """Checks whether the next user that joins this game will be considered a
    'player' or a 'spectator'. Users are considered spectators if there are 
    at least two players in the lobby.
    If the match is over, the role will be an empty string."""
    game = models.GameLobby.objects.get(pk=game_code)
    if game.is_over:
        return ""

    num_of_players, _ = get_num_of_users(game_code)
    if num_of_players < 2:
        return "player"
    else:
        return "spectator"


def close_if_all_players_left(game_code):
    """Cleans up the database if all players have left the lobby.
    Returns true if the lobby was closed, and false otherwise. Returns false if
    the lobby did not exist."""
    if chess_manager.does_match_exist(game_code):
        num_of_players, _ = get_num_of_users(game_code)
        if num_of_players == 0:
            chess_manager.delete_match(game_code)
            return True
    else:
        return False


def disconnect_user(user_id):
    """Removes this user from the database."""
    try:
        user = models.ChessUser.objects.get(pk=user_id)
        user.delete()
    except models.ChessUser.DoesNotExist:
        print("User cannot be deleted because he does not exist.")


def get_num_of_users(game_code):
    """Returns the number of players and spectators in this match in the format 
    `players, spectators`."""
    users = models.ChessUser.objects.filter(game_code=game_code)
    num_of_players = len(users.exclude(color="").all())
    num_of_spectators = len(users) - num_of_players
    return num_of_players, num_of_spectators
    
