from src.experiments.chess_core.pieces.p_base import BasePiece


class BishopPiece(BasePiece):
    """A class representing a bishop chess piece."""
    
    def __init__(self):
        """Creates a bishop object."""
        super().__init__("X", [8])

    def get_valid_moves(self, start, match):

        # Get all available diagonal positions

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked on any side

        return super().get_valid_moves(start, match)