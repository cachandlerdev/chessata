from src.experiments.chess_core.pieces.p_base import BasePiece


class RookPiece(BasePiece):
    """A class representing a rook chess piece."""
    
    def __init__(self):
        """Creates a rook object."""
        self._movement_range = 8


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        moves = self._get_valid_cross_moves(start, match)
        return moves
        
