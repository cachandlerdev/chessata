from ..structs.game_state import GameState
from ..structs.piece_type import PieceType
from ..structs.move_type import MoveType
from ..pieces.p_bishop import BishopPiece
from ..pieces.p_king import KingPiece
from ..pieces.p_knight import KnightPiece
from ..pieces.p_pawn import PawnPiece
from ..pieces.p_queen import QueenPiece
from ..pieces.p_rook import RookPiece
from .. import board_utils
import copy


"""A class used to handle rules about the chess game mode."""


def move_piece_at_pos(match, start, end, promotion_type=PieceType.QUEEN):
    """Updates the current match based on the movement of a particular piece
    from `start` position to `end` if the move is valid for that kind of 
    piece. We check if moves are valid.

    Args:
        match (Match): A chess match with info about the board and current
        state.
        start (str): The current position of the piece. E.g. `b3`, `d6`
        end (str): The final position of the piece.
        promotion_type (PieceType, optional): Used to determine what kind of
        promotion to make if we are promoting a pawn this move. Defaults to
        queen promotions.

    Raises:
        ValueError: If there is not a valid piece at `start`.
        ValueError: If `start` and `end` point to the same piece.
        ValueError: If this is an illegal move.

    Returns:
        list: The new board array after the move was made.
    """
    piece_num = board_utils.get_piece_at_pos(match.board, start)

    try:
        piece = get_piece_object(piece_num)
    except ValueError:
        raise ValueError("Invalid piece number.")

    if start == end:
        raise ValueError("Start and end positions match.")

    moves = piece.get_valid_moves(start, match)
    moves = _remove_friendly_check_moves(moves, start, promotion_type, match)
    if end in moves:
        type = _identify_move_type(start, end, match.board)
        match type:
            case MoveType.EN_PASSANT:
                _update_match_en_passant(start, end, match, piece_num)
            case MoveType.PROMOTION:
                _update_match_promotion(start, end, match, piece_num, promotion_type)
            case MoveType.CASTLING:
                _update_match_castling(start, end, match, piece_num)
            case MoveType.REGULAR:
                _update_match_regular(start, end, match, piece_num)
        
        _update_match_state(start, end, match, piece_num, type)
    else:
        raise ValueError("Illegal move.")


def is_players_piece(pos, is_white, board):
    """Checks whether the piece located at the given position belongs to
    this player."""
    piece = board_utils.get_piece_at_pos(board, pos)
    if is_white:
        return piece > 0
    else:
        return piece < 0


def _update_match_state(start, end, match, piece_num, type):
    """Updates the match state if necesssary to keep track of things like 
    the king moving for the first time, pawns exposing themselves to en 
    passant, and rooks moving for the first time."""
    is_white = (piece_num > 0)

    # We unexpose any non-attacked friendly pawns first to avoid overwriting
    # newly moved pawns
    match.unexpose_friendly_pawns_to_en_passant(is_white)
    
    if abs(piece_num) == 6:
        if type == MoveType.CASTLING:
            is_kingside = (end[0] > start[0])
            match.set_king_has_moved(is_white)
            match.set_rook_has_moved(is_white, is_kingside)
        else:
            match.set_king_has_moved(is_white)

    if abs(piece_num) == 1:
        length = int(end[1]) - int(start[1])
        if abs(length) == 2:
            match.expose_pawn_to_en_passant(is_white, end)

    if abs(piece_num) == 2:
        is_kingside = (start[0] == "h")
        match.set_rook_has_moved(is_white, is_kingside)
 

def resolve_game_state(match, is_white_turn, promotion_type):
    """Determines whether the specified match is over yet."""
    white_king_pos = board_utils.find_piece_pos(6, match.board)
    white_has_moves = player_has_moves(match, True, promotion_type)
    if is_in_check(white_king_pos, True, match):
        if white_has_moves:
            return GameState.WHITE_CHECK
        else:
            return GameState.BLACK_WIN

    black_king_pos = board_utils.find_piece_pos(-6, match.board)
    black_has_moves = player_has_moves(match, False, promotion_type)
    if is_in_check(black_king_pos, False, match):
        if black_has_moves:
            return GameState.BLACK_CHECK
        else:
            return GameState.WHITE_WIN
    
    # Neither player is in check
    if is_white_turn:
        current_has_moves = white_has_moves
    else:
        current_has_moves = black_has_moves
    
    if current_has_moves:
        return GameState.NOT_OVER
    else:
        return GameState.STALEMATE


def player_has_moves(match, is_white, promotion_type):
    """Checks whether the given player has moves for this match."""
    moves = get_player_moves(match, is_white, promotion_type)
    for key, value in moves.items():
        if len(value) > 0:
            return True
    return False


def get_player_moves(match, is_white, promotion_type):
    """Gets all possible moves for the given player based on the current 
    match. Moves that would put/keep the friendly king in check are 
    disallowed. Returned in the format {start1: [m1, m2, m3], start2: [m1]}"""
    indexes = _get_player_piece_indexes(match.board, is_white)

    total_moves = {}
    for index in indexes:
        piece_pos = board_utils.get_pos_from_index(index)
        piece_value = board_utils.get_piece_at_pos(match.board, piece_pos)
        piece = get_piece_object(piece_value)
        all_moves = piece.get_valid_moves(piece_pos, match)
        safe_moves = _remove_friendly_check_moves(all_moves, piece_pos, promotion_type, match)
        total_moves[piece_pos] = safe_moves
    return total_moves


def _get_player_piece_indexes(board, is_white):
    """Gets the board index of every one of the white/black player's pieces.
    """
    piece_indexes = []
    for i, p in enumerate(board):
        if is_white:
            if p > 0:
                piece_indexes.append(i)
        else:
            if p < 0:
                piece_indexes.append(i)
    return piece_indexes


def _remove_friendly_check_moves(all_moves, start, promotion_type, match):
    """Removes all moves that would put the friendly king in check and 
    returns the resulting moves."""
    piece_to_move = board_utils.get_piece_at_pos(match.board, start)
    check_white_king = (piece_to_move > 0)
    valid_moves = []
    
    for move in all_moves:
        type = _identify_move_type(start, move, match.board)
        invalid_castling = (type == MoveType.CASTLING) and (
            _is_illegal_castling_move(start, move, check_white_king, match))
        invalid_regular = _is_illegal_regular_move(start, move, check_white_king, type, promotion_type, match)
        if not invalid_castling and not invalid_regular:
            valid_moves.append(move)
    return valid_moves


def _is_illegal_regular_move(start, end, check_white_king, move_type, promotion_type, match):
    """Checks whether making this move would put the friendly king in check,
    and therefore be an illegal move. Note that this function does not
    handle castling cases."""
    new_match = copy.deepcopy(match)
    this_piece = board_utils.get_piece_at_pos(new_match.board, start)
    match move_type:
        case MoveType.EN_PASSANT:
            _update_match_en_passant(start, end, new_match, this_piece)
        case MoveType.PROMOTION:
            _update_match_promotion(start, end, new_match, this_piece, promotion_type)
        case MoveType.REGULAR:
            _update_match_regular(start, end, new_match, this_piece)

    king_value = 6 if check_white_king else -6
    king_pos = board_utils.find_piece_pos(king_value, new_match.board)
    return is_in_check(king_pos, check_white_king, new_match)


def _is_illegal_castling_move(start, end, check_white_king, match):
    """Looks at whether making this castling move would be legal with regard 
    to check rules. Namely, we determine whether the king is trying to 
    castle out of, through, or into check."""
    x = 1 if start[0] < end[0] else -1
    if is_in_check(start, check_white_king, match):
        # Castle out of check
        return True

    middle = board_utils.relative_to_absolute_pos(start, (x, 0))
    if is_in_check(middle, check_white_king, match):
        # Castle through check
        return True
    
    if is_in_check(end, check_white_king, match):
        # Castle into check
        return True
    
    return False


def is_in_check(pos, is_white, match):
    """Checks whether a king at this position for the specified match is
    in check. Note that the king doesn't actually *have* to be at this 
    position, as we're testing whether he *would* be in check if he moved 
    here."""
    if _is_in_cross_check(pos, is_white, match):
        return True
    if _is_in_diagonal_check(pos, is_white, match):
        return True
    if _is_in_knight_check(pos, is_white, match):
        return True
    return False


def _is_in_cross_check(pos, is_white, match):
    """Checks whether a king located at this position would be in check from
    rooks, queens, or the other king."""
    if is_white:
        enemy_pieces = [-2, -5, -6]
    else:
        enemy_pieces = [2, 5, 6]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        if _is_in_directional_check(pos, is_white, direction, 
                                         enemy_pieces, match.board):
            return True
    return False


def _is_in_diagonal_check(pos, is_white, match):
    """Checks whether a king located at this position would be in check from
    bishops, queens, pawns, or the other king."""
    if is_white:
        enemy_pieces = [-1, -4, -5, -6]
    else:
        enemy_pieces = [1, 4, 5, 6]
    
    directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    for direction in directions:
        if _is_in_directional_check(pos, is_white, direction, 
                                         enemy_pieces, match.board):
            return True
    return False

def _is_in_directional_check(pos, is_white, direction, enemy_pieces, board):
    """Checks whether a king located at this position would be in check
    for the specified list of enemy pieces in the given direction.
    Note: You must specify whether the enemy pieces are white or black by
    inputting positive/negative piece numbers!"""
    square = pos
    distance = 0
    while (square[0] >= "a" and square[0] <= "h") and (
        int(square[1]) >= 1 and int(square[1]) <= 8):
        try:
            new_square = board_utils.relative_to_absolute_pos(square, direction)
        except ValueError:
            # We've reached the edge of the board
            return False

        distance += 1
        square_piece = board_utils.get_piece_at_pos(board, new_square)
        if square_piece != 0:
            if square_piece in enemy_pieces:
                match abs(square_piece):
                    # Pawn
                    case 1:
                        right_distance = (distance == 1)
                        y_to_check = 1 if is_white else -1
                        right_direction = direction[1] == y_to_check
                        return right_distance and right_direction
                    # King
                    case 6:
                        return (distance == 1)
                    # Others
                    case _:
                        return True
            # Even if he's not in check, we still stop looking in this 
            # direction because we found the first piece in this direction.
            return False
        square = new_square
    # Checked all squares in this direction
    return False


def _is_in_knight_check(pos, is_white, match):
    """Checks whether a king located at this position would be in check from
    knights."""
    transforms = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), 
                  (-1, -2), (-2, -1)]
    for transform in transforms:
        enemy_knight = -3 if is_white else 3
        try:
            square = board_utils.relative_to_absolute_pos(pos, transform)
        except ValueError:
            # This square doesn't exist
            continue
        square_piece = board_utils.get_piece_at_pos(match.board, square)
        if square_piece == enemy_knight:
            return True

    return False


def _update_match_en_passant(start, end, match, piece_num):
    """Updates the specified match board to account for an en passant move."""
    start_index = board_utils.get_board_pos_index(start)
    match.board[start_index] = 0
    end_index = board_utils.get_board_pos_index(end)
    match.board[end_index] = piece_num
    
    transform = board_utils.absolute_to_relative_pos(start, end)
    x = 1 if transform[0] > 0 else -1
    other_pawn_square = board_utils.relative_to_absolute_pos(start, (x, 0))
    other_pawn_index = board_utils.get_board_pos_index(other_pawn_square)
    match.board[other_pawn_index] = 0


def _update_match_promotion(start, end, match, piece_num, promotion_type):
    """Updates the specified match board to account for a pawn promotion move."""
    if promotion_type == PieceType.KING or promotion_type == PieceType.PAWN:
        raise ValueError("Invalid promotion type.")
    if abs(piece_num) != 1:
        raise ValueError("Only pawns can be promoted.")
    
    start_index = board_utils.get_board_pos_index(start)
    match.board[start_index] = 0
    end_index = board_utils.get_board_pos_index(end)
    
    factor = 1 if piece_num > 0 else -1
    match.board[end_index] = factor * promotion_type.value


def _update_match_castling(start, end, match, piece_num):
    """Updates the specified match board to account for a castling move."""
    kingside = start[0] < end[0]

    if kingside:
        new_rook_pos = board_utils.relative_to_absolute_pos(start, (1, 0))
        new_king_pos = board_utils.relative_to_absolute_pos(start, (2, 0))
        old_rook_pos = f"h{start[1]}"
    else:
        new_rook_pos = board_utils.relative_to_absolute_pos(start, (-1, 0))
        new_king_pos = board_utils.relative_to_absolute_pos(start, (-2, 0))
        old_rook_pos = f"a{start[1]}"
    
    old_rook_index = board_utils.get_board_pos_index(old_rook_pos)
    old_king_index = board_utils.get_board_pos_index(start)
    new_rook_index = board_utils.get_board_pos_index(new_rook_pos)
    new_king_index = board_utils.get_board_pos_index(new_king_pos)

    rook_value = match.board[old_rook_index]
    match.board[old_rook_index] = 0
    match.board[old_king_index] = 0
    match.board[new_rook_index] = rook_value
    match.board[new_king_index] = piece_num


def _update_match_regular(start, end, match, piece_num):
    """Updates the specified match board to account for a regular move."""
    start_index = board_utils.get_board_pos_index(start)
    match.board[start_index] = 0
    end_index = board_utils.get_board_pos_index(end)
    match.board[end_index] = piece_num


def get_piece_object(num):
    """Returns a piece object (e.g. King, Pawn, etc.) based on the specified 
    piece number."""
    match abs(num):
        case 1:
            return PawnPiece()
        case 2:
            return RookPiece()
        case 3:
            return KnightPiece()
        case 4:
            return BishopPiece()
        case 5:
            return QueenPiece()
        case 6:
            return KingPiece()
        case _:
            raise ValueError("Invalid piece number.")


def _identify_move_type(start, end, board):
    """Tries to identify the type of move that was just made. The special 
    move types we look for are en passants, pawn promotions, and castling.
    If it wasn't one of these, we assume it was a regular move."""
    this_piece = board_utils.get_piece_at_pos(board, start)
    
    if abs(this_piece) == 1:
        if _is_pawn_promotion_move(start, end, this_piece):
            return MoveType.PROMOTION
        if _is_en_passant_move(start, end, board, this_piece):
            return MoveType.EN_PASSANT
    elif abs(this_piece) == 6:
        if _is_castling_move(start, end, board, this_piece):
            return MoveType.CASTLING
    
    return MoveType.REGULAR


def _is_en_passant_move(start, end, board, this_piece):
    """Returns true if this was an en passsant move."""
    if this_piece > 0:
        y = 1
    else:
        y = -1
    
    transform = board_utils.absolute_to_relative_pos(start, end)
    is_left_attack = (transform[0] == -1) and (transform[1] == y)
    is_right_attack = (transform[0] == 1) and (transform[1] == y)
    
    if is_left_attack:
        left_square = board_utils.relative_to_absolute_pos(start, (-1, 0))
        square_piece = board_utils.get_piece_at_pos(board, left_square)
        if (abs(square_piece) == 1) and not (
            board_utils.is_piece_friendly(this_piece, square_piece)):
            return True
    
    if is_right_attack:
        right_square = board_utils.relative_to_absolute_pos(start, (1, 0))
        square_piece = board_utils.get_piece_at_pos(board, right_square)
        if (abs(square_piece) == 1) and not (
            board_utils.is_piece_friendly(this_piece, square_piece)):
            return True

    return False


def _is_pawn_promotion_move(start, end, this_piece):
    """Returns true if this was a pawn promotion move."""
    if abs(this_piece) != 1:
        return False

    if this_piece > 0:
        right_start = (int(start[1]) == 7)
        right_end = (int(end[1]) == 8)
        return right_start and right_end
    else:
        right_start = (int(start[1]) == 2)
        right_end = (int(end[1]) == 1)
        return right_start and right_end


def _is_castling_move(start, end, board, this_piece):
    """Returns true if this was a castling move. We assume the piece at the
    start position was a king."""
    if this_piece > 0:
        right_row = (int(start[1]) == 1)
    else:
        right_row = (int(start[1]) == 8)
    
    stay_on_row = (start[1] == end[1])

    move_length = abs(ord(start[0]) - ord(end[0]))
    right_length = (move_length == 2)
    
    return right_row and stay_on_row and right_length
