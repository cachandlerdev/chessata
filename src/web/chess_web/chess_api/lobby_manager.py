import secrets

from . import models


def create_user(game_code, username):
    """Creates a user for the match with the specified game code and username,
    and returns the user ID and game role (player/spectator). Returns empty 
    strings if the user couldn't be created."""
    if game_code == "" or username == "":
        return "", ""
    
    user_id_length = 12

    user_id = secrets.token_urlsafe(user_id_length)
    role = _get_next_user_role(game_code)

    return user_id, role


def add_user_to_match(user_id, game_code, username):
    """Adds this user to the ChessUser database. We return his color (a 
    spectator's color is the empty string).
    Throws an `IntegrityError` if the user couldn't be saved."""
    # TODO: Handle spectators 
    other_users = models.ChessUser.objects.filter(game_code=game_code)
    num_of_other_players = len(other_users.exclude(color="").all())
    
    # TODO: Add an option to select the player color
    if num_of_other_players == 0:
        color = "white"
    elif num_of_other_players == 1:
        color = "black"
    # Save to database
    chess_user = models.ChessUser(user_id=user_id, 
                                username=username,
                                game_code=game_code,
                                color=color)
    chess_user.save()
    
    return chess_user, color


def _get_next_user_role(game_code):
    """Checks whether the next user that joins this game will be considered a
    'player' or a 'spectator'. Users are considered spectators if there are 
    at least two players in the lobby."""
    # TODO
    pass


def close_if_all_players_left(user_id, game_code):
    """Cleans up the database if all players have left the lobby.
    Returns true if the lobby was closed, and false otherwise."""
    # TODO
    pass


def is_game_in_progress(game_code):
    """Checks whether this lobby is currently in progress."""
    return True


def disconnect_user(user_id):
    """Removes this user from the database."""
    user = models.ChessUser.objects.get(pk=user_id)
    user.delete()
