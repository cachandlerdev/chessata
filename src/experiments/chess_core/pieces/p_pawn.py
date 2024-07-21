from src.experiments.chess_core.pieces.p_base import BasePiece


class PawnPiece(BasePiece):
    """A class representing a pawn chess piece."""
    
    def __init__(self):
        """Creates a pawn object."""
        super().__init__("|", [1, 2], "V")


    def get_valid_moves(self, start, board):
        # Check if the piece has moved
        # If not, it can move 2 spaces forward
        # Else, just one

        # Check if there are enemy pieces on diagonals
        # Use self.is_white to see what's friendly or not

        # Check if it's blocked in front

        # Don't forget en passant rules
        
        # This is a special case where you might need to write a custom 
        # collision checker for attack rules.
        return super().get_valid_moves(start, board)