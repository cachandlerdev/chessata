from src.experiments.chess_core.pieces.p_base import BasePiece


class KnightPiece(BasePiece):
    def get_valid_moves(self, start, board):

        # Get all available L positions

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked when making L's

        return super().get_valid_moves(start, board)