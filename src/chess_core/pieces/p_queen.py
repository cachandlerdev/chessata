from .p_base import BasePiece


class QueenPiece(BasePiece):
    """A class representing a queen chess piece."""
    
    def __init__(self):
        """Creates a queen object."""
        self._movement_range = 8


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        moves = self._get_valid_cross_moves(start, match)
        moves.extend(self._get_valid_diagonal_moves(start, match))
        return moves