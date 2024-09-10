from . import models
from . import lobby_manager
import json
from chess_core.structs.game_state import GameState
import chess_core.game_match.match_chess as chess_match
import chess_core.game_mode.gamemode_chess as chess_mode
import chess_core.structs.piece_type as promotion


def create_new_match(game_code):
    """Creates a new chess match in the database with the specified game code."""
    match = chess_match.ChessMatch()
    _save_match_state(game_code, match, True)


def does_match_exist(game_code):
    """Checks whether there is an ongoing match in the database with this game 
    code."""
    try:
        models.GameLobby.objects.get(pk=game_code)
        return True
    except models.GameLobby.DoesNotExist:
        return False


def is_match_in_progress(game_code):
    """Checks whether this match is currently ongoing. Returns false if the game
    doesn't exist."""
    if does_match_exist(game_code):
        game = models.GameLobby.objects.get(pk=game_code)
        return not game.is_over
    else:
        return False


def _load_match(game_code):
    """Reconstructs the chess match using the information stored in the 
    database. 
    Returns the match and if it's white's turn, or None if the match doesn't 
    exist."""
    if does_match_exist(game_code):
        game = models.GameLobby.objects.get(pk=game_code)
        board_data = json.loads(game.board)
        allow_en_passant_data = json.loads(game.allow_en_passant)
        has_king_moved_data = json.loads(game.has_king_moved)
        has_rook_moved_data = json.loads(game.has_rook_moved)
        match = chess_match.ChessMatch(board=board_data, 
                                       allow_en_passant=allow_en_passant_data,
                                       has_king_moved=has_king_moved_data,
                                       has_rook_moved=has_rook_moved_data)
        return match, game.is_white_turn
    else:
        return None, False
    


def make_match_move(game_code, start, end, user_id, promotion_type="queen"):
    """Looks up the chess match with this game code and tries to make the move
    for the specified player.
    Returns `true, ''` if the move could be made, and `false, reason` if not."""
    promotion = promotion_to_enum(promotion_type)
    match, is_white_turn = _load_match(game_code)
    if match is None:
        return False, "The match does not exist."

    if _is_correct_player(game_code, is_white_turn, user_id):
        if chess_mode.is_players_piece(start, is_white_turn, match.board):
            try:
                chess_mode.move_piece_at_pos(match, start, end, promotion)
                _save_match_state(game_code, match, not is_white_turn)
                return True, ""
            except ValueError as e:
                reason = getattr(e, 'message', repr(e))
                return False, reason
        else:
            return False, "This is not your piece."
    else:
        return False, "It is not your turn."


def promotion_to_enum(str):
    """Converts the promotion string to an enum."""
    match str:
        case "queen":
            return promotion.PieceType.QUEEN
        case "bishop":
            return promotion.PieceType.BISHOP
        case "knight":
            return promotion.PieceType.KNIGHT
        case "rook":
            return promotion.PieceType.ROOK
        case _:
            # If all else fails, default to the queen
            return promotion.PieceType.QUEEN


def end_state_to_str(state):
    """Converts the end state enum to a string."""
    match state:
        case GameState.NOT_OVER:
            return "not over"
        case GameState.WHITE_CHECK:
            return "white check"
        case GameState.BLACK_CHECK:
            return "black check"
        case GameState.STALEMATE:
            return "stalemate"
        case GameState.WHITE_WIN:
            return "white win"
        case GameState.BLACK_WIN:
            return "black win"


def _save_match_state(game_code, match, is_white_turn):
    """Saves this match's state to the database. Normally, we return an empty 
    string, but if the match just ended, we return either 'white_win', 
    'black win', or 'stalemate'."""
    # TODO: Support other promotion types
    end_state = chess_mode.resolve_game_state(match, is_white_turn, promotion.PieceType.QUEEN)
    end_state_str = end_state_to_str(end_state)

    black_win = end_state == GameState.BLACK_WIN
    white_win = end_state == GameState.WHITE_WIN
    stalemate = end_state == GameState.STALEMATE
    is_over = (black_win or white_win or stalemate)
    
    board_data = json.dumps(match.board)
    allow_en_passant_data = json.dumps(match._allow_en_passant)
    has_king_moved_data = json.dumps(match._has_king_moved)
    has_rook_moved_data = json.dumps(match._has_rook_moved)
    game = models.GameLobby(game_code=game_code, 
                                is_over=is_over, 
                                is_white_turn=is_white_turn,
                                board=board_data,
                                allow_en_passant=allow_en_passant_data, 
                                has_king_moved=has_king_moved_data, 
                                has_rook_moved=has_rook_moved_data,
                                match_state=end_state_str)
    game.save()
    

def end_match(game_code, match_state):
    """Used to prematurely end matches."""
    if does_match_exist(game_code):
        models.GameLobby.objects.filter(pk=game_code).update(
            is_over=True,
            match_state=match_state,
        )
    
        

def get_game_state(game_code):
    """Returns a JSON formatted object for API communication describing the
    current state of this match. Returns an empty string if the game doesn't 
    exist."""
    if does_match_exist(game_code):
        game = models.GameLobby.objects.get(pk=game_code)
        # Get turn id
        if game.is_white_turn:
            users = models.ChessUser.objects.filter(game_code=game_code)
            player = users.get(color="white")
        else:
            users = models.ChessUser.objects.filter(game_code=game_code)
            player = users.get(color="black")
        
        player_turn_id = player.user_id

        json_decoder = json.decoder.JSONDecoder()
        board = json_decoder.decode(game.board)
        allow_en_passant = json_decoder.decode(game.allow_en_passant)
        has_king_moved = json_decoder.decode(game.has_king_moved)
        has_rook_moved = json_decoder.decode(game.has_rook_moved)
        match_state = game.match_state
        data = {
            "player_turn_id": player_turn_id,
            "match_state": match_state,
            "board": board,
            "allow_en_passant": allow_en_passant,
            "has_king_moved": has_king_moved,
            "has_rook_moved": has_rook_moved,
        }
        return data
    return ""


def _is_correct_player(game_code, is_white_turn, user_id):
    """Returns true if this player can legally make a move this turn."""
    if is_white_turn:
        users = models.ChessUser.objects.filter(game_code=game_code)
        player = users.get(color="white")
        return player.user_id == user_id
    else:
        users = models.ChessUser.objects.filter(game_code=game_code)
        player = users.get(color="black")
        return player.user_id == user_id
    

def delete_match(game_code):
    """Deletes the match with the specified game code."""
    game = models.GameLobby.objects.get(pk=game_code)
    game.delete()
