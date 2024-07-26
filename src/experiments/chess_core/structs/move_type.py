from enum import Enum

class MoveType(Enum):
    REGULAR = 1
    CASTLING = 2
    EN_PASSANT = 3
    PROMOTION = 4