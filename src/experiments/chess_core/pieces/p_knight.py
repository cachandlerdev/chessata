from src.experiments.chess_core.pieces.p_base import BasePiece


class KnightPiece(BasePiece):
    """A class representing a knight chess piece."""
    
    def __init__(self):
        """Creates a knight object."""
        super().__init__("L")


    def get_valid_moves(self, start, match):

        # Get all available L positions

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked when making L's

        return super().get_valid_moves(start, match)