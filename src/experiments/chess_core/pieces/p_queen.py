from src.experiments.chess_core.pieces.p_base import BasePiece


class QueenPiece(BasePiece):
    """A class representing a queen chess piece."""
    
    def __init__(self):
        """Creates a queen object."""
        super().__init__("+X", [8])


    def get_valid_moves(self, start, match):

        # Get all available directional moves

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked when moving

        return super().get_valid_moves(start, match)