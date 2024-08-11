from enum import Enum

class GameState(Enum):
    NOT_OVER = 1
    WHITE_CHECK = 2
    BLACK_CHECK = 3
    STALEMATE = 4
    WHITE_WIN = 5
    BLACK_WIN = 6
