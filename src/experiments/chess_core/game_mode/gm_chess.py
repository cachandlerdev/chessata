from src.experiments.chess_core.structs.move_type import MoveType
from src.experiments.chess_core.pieces.p_bishop import BishopPiece
from src.experiments.chess_core.pieces.p_king import KingPiece
from src.experiments.chess_core.pieces.p_knight import KnightPiece
from src.experiments.chess_core.pieces.p_pawn import PawnPiece
from src.experiments.chess_core.pieces.p_queen import QueenPiece
from src.experiments.chess_core.pieces.p_rook import RookPiece
import src.experiments.chess_core.board_utils as board_utils


class ChessGameMode:
    """A class used to handle rules about the chess game mode."""
    def __init__(self):
        # TODO: Figure out how we're storing matches. Is it on the game mode?
        # A separate 'game_manager' class? Not sure.
        self._matches = []
    

    def move_piece_at_pos(self, match, start, end):
        """Updates the current match based on the movement of a particular piece
        from `start` position to `end` if the move is valid for that kind of 
        piece. We check if moves are valid.

        Args:
            match (Match): A chess match with info about the board and current
            state.
            start (str): The current position of the piece. E.g. `b3`, `d6`
            end (str): The final position of the piece.

        Raises:
            ValueError: If there is not a valid piece at `start`.
            ValueError: If `start` and `end` point to the same piece.
            ValueError: If this is an illegal move.

        Returns:
            list: The new board array after the move was made.
        """
        piece_num = board_utils.get_piece_at_pos(match.board, start)

        try:
            piece = self.get_piece_object(piece_num)
        except ValueError:
            raise ValueError("Invalid piece number.")

        if start == end:
            raise ValueError("Start and end positions match.")

        valid_moves = piece.get_valid_moves(start, match)
        if end in valid_moves:
            type = self._identify_move_type(start, end, match.board)
            match type:
                case MoveType.EN_PASSANT:
                    self._update_match_en_passant(start, end, match, piece_num)
                case MoveType.PROMOTION:
                    self._update_match_promotion(start, end, match, piece_num)
                case MoveType.CASTLING:
                    self._update_match_castling(start, end, match, piece_num)
                case MoveType.REGULAR:
                    self._update_match_regular(start, end, match, piece_num)
            # TODO: Look for check/checkmate
        else:
            raise ValueError("Illegal move.")
    
   
    def _update_match_en_passant(self, start, end, match, piece_num):
        """Updates the specified match board to account for an en passant move."""
        # TODO
        start_index = board_utils.get_board_pos_index(start)
        match.board[start_index] = 0
        end_index = board_utils.get_board_pos_index(end)
        match.board[end_index] = piece_num
        
        transform = board_utils.absolute_to_relative_pos(start, end)
        x = 1 if transform[0] > 0 else -1
        other_pawn_square = board_utils.relative_to_absolute_pos(start, (x, 0))
        other_pawn_index = board_utils.get_board_pos_index(other_pawn_square)
        match.board[other_pawn_index] = 0
    

    def _update_match_promotion(self, start, end, match, piece_num):
           """Updates the specified match board to account for a pawn promotion move."""
           # TODO
           pass
    
    
    def _update_match_castling(self, start, end, match, piece_num):
           """Updates the specified match board to account for a castling move."""
           # TODO
           pass
 

    def _update_match_regular(self, start, end, match, piece_num):
        """Updates the specified match board to account for a regular move."""
        start_index = board_utils.get_board_pos_index(start)
        match.board[start_index] = 0
        end_index = board_utils.get_board_pos_index(end)
        match.board[end_index] = piece_num
    

    def get_piece_object(self, num):
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
    

    def _identify_move_type(self, start, end, board):
        """Tries to identify the type of move that was just made. The special 
        move types we look for are en passants, pawn promotions, and castling.
        If it wasn't one of these, we assume it was a regular move."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        
        if abs(this_piece) == 1:
            # Pawn
            if self._is_pawn_promotion_move(start, end, board, this_piece):
                return MoveType.PROMOTION
            if self._is_en_passant_move(start, end, board, this_piece):
                return MoveType.EN_PASSANT
        elif abs(this_piece) == 6:
            # King
            if self._is_castling_move(start, end, board, this_piece):
                return MoveType.CASTLING
        
        return MoveType.REGULAR

    
    def _is_en_passant_move(self, start, end, board, this_piece):
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
 

    def _is_pawn_promotion_move(self, start, end, board, this_piece):
        """Returns true if this was a pawn promotion move."""
        # TODO
        return False

    def _is_castling_move(self, start, end, board, this_piece):
        """Returns true if this was a castling move."""
        # TODO
        return False
