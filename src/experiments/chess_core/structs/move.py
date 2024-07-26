from dataclasses import dataclass

from src.experiments.chess_core.structs.move_type import MoveType


@dataclass(frozen=True)
class Move:
    """Represents a chess piece move from point A to point B."""
    start: str
    end: str
    type: MoveType = MoveType.REGULAR