from src.experiments.chess_core.structs.move import Move
from src.experiments.chess_core.structs.move_type import MoveType
from src.experiments.chess_core.pieces.p_base import BasePiece
import src.experiments.chess_core.board_utils as board_utils


class PawnPiece(BasePiece):
    """A class representing a pawn chess piece."""
    
    def __init__(self):
        """Creates a pawn object."""
        super().__init__("|", [1, 2], "V")


    def get_valid_moves(self, start, match):
        # Check if the piece has moved
        # If not, it can move 2 spaces forward
        # Else, just one

        # Check if there are enemy pieces on diagonals
        # Use self.is_white to see what's friendly or not

        # Check if it's blocked in front

        # Don't forget en passant rules
        # https://www.chess.com/terms/en-passant
        
        # This is a special case where you might need to write a custom 
        # collision checker for attack rules.
        
        # TODO: Add pawn promotion
        return super().get_valid_moves(start, match)
    
    
    def _get__movement_range(self, pos, board):
        this_piece = board_utils.get_piece_at_pos(board, pos)
        if this_piece > 0:
            # White
            if int(pos[1]) == 2:
                return self._movement_range[1]
            else:
                return self._movement_range[0]
        else:
            # Black
            if int(pos[1]) == 7:
                return self._movement_range[1]
            else:
                return self._movement_range[0]
    

    def _get_valid_en_passant_moves(self, start, match):
        """Returns a list of valid en passant attack moves."""
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        moves = []
        
        if this_piece > 0:
            # White on valid row
            check_moves = (int(start[1]) == 5)
            y = 1
        else:
            # Black on valid row
            check_moves = (int(start[1]) == 4)
            y = -1
            
        if check_moves:
            left_square = self._relative_to_absolute_pos(start, (-1, 0))
            right_square = self._relative_to_absolute_pos(start, (-1, 0))

            left_piece = board_utils.get_piece_at_pos(match.board, left_square)
            right_piece = board_utils.get_piece_at_pos(match.board, right_square)
            pieces = [left_piece, right_piece]
            
            for piece in pieces:
                if abs(piece) == 1 and not (
                    board_utils.is_piece_friendly(this_piece, piece)):
                    end = self._relative_to_absolute_pos(piece, (0, y))
                    if match.is_valid_en_passant(start, piece, end):
                        move = Move(start, end, MoveType.EN_PASSANT)
                        moves.append(move)
        return moves