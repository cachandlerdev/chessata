from src.experiments.chess_core.pieces.p_base import BasePiece


class BishopPiece(BasePiece):
    """A class representing a bishop chess piece."""
    
    def __init__(self):
        """Creates a bishop object."""
        self._movement_range = 8


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        moves = self._get_valid_diagonal_moves(start, match)
        return moves