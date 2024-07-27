from src.experiments.chess_core.pieces.p_base import BasePiece
import src.experiments.chess_core.board_utils as board_utils


class KnightPiece(BasePiece):
    """A class representing a knight chess piece."""


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        moves = self._get_valid_L_moves(start, match)
        return moves
    
    
    def _get_valid_L_moves(self, start, match):
        """Returns a list of valid L move positions for this piece based on
        the specified board and start position."""
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        transforms = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), 
                          (-1, -2), (-2, -1)]
        valid_moves = []
        
        for transform in transforms:
            try:
                square = board_utils.relative_to_absolute_pos(start, transform)
                square_piece = board_utils.get_piece_at_pos(match.board, square)
                if square_piece == 0:
                    valid_moves.append(square)
                else:
                    if not board_utils.is_piece_friendly(this_piece, square_piece):
                        valid_moves.append(square)
            except ValueError:
                # Skip this invalid move
                continue
            
        return valid_moves
