from src.experiments.chess_core.pieces.p_base import BasePiece


class KingPiece(BasePiece):
    """A class representing a king chess piece."""
    
    def __init__(self):
        """Creates a king object."""
        self._movement_range = 1


    def get_valid_moves(self, start, match):
        # TODO: Add castling
            # Make sure castling can only happen with friendly rooks
        # TODO: Add king check
        # TODO: Add checkmate (probably on the gamemode class)
        super().get_valid_moves(start, match)
        moves = self._get_valid_cross_moves(start, match)
        moves.extend(self._get_valid_diagonal_moves(start, match))
        return moves