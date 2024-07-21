from src.experiments.chess_core.pieces.p_base import BasePiece


class KingPiece(BasePiece):
    """A class representing a king chess piece."""
    
    def __init__(self):
        """Creates a king object."""
        super().__init__("+X", [1])


    def get_valid_moves(self, start, board):

        # Get all available 8 positions

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked on any side

        # You will need to add king checking here and disable invalid moves

        # Don't forget that weird move where the king and the rook swap places

        # And make sure the swap is with friendly kings and friendly rooks (no sneaky black rook swapping with white king business)

        return super().get_valid_moves(start, board)