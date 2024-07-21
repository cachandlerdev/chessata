from abc import ABC, abstractmethod


class BasePiece:
    """The abstract base class for all chess pieces."""

    def __init__(self, is_white):
        self.is_white = is_white

    
    @abstractmethod
    def get_valid_moves(self, start, board):
        """Returns a list of valid moves for this piece based on the specified
        board and start position."""
        # TODO: Add king check based on movement
        # TODO: Make sure pieces stay on the board (probably a helper function on this class that gets used by subclasses)
        pass