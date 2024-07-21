from src.experiments.chess_core.pieces.p_base import BasePiece


class BishopPiece(BasePiece):

    def get_valid_moves(self, start, board):

        # Get all available diagonal positions

        # Use self.is_white to see what's friendly or not

        # Check if it's blocked on any side

        return super().get_valid_moves(start, board)