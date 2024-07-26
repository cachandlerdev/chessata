from src.experiments.chess_core.pieces.p_bishop import BishopPiece
from src.experiments.chess_core.pieces.p_king import KingPiece
from src.experiments.chess_core.pieces.p_knight import KnightPiece
from src.experiments.chess_core.pieces.p_pawn import PawnPiece
from src.experiments.chess_core.pieces.p_queen import QueenPiece
from src.experiments.chess_core.pieces.p_rook import RookPiece
import src.experiments.chess_core.board_utils as board_utils


class ChessGameMode:
    """A class used to handle rules about the chess game mode."""
    def __init__(self):
        self._matches = []


    def start_match(self):
        """Starts a chess match."""
        # TODO
        # add to the matches list
        pass
    

    def move_piece_at_pos(self, match, start, end):
        """Updates the current match based on the movement of a particular piece
        from `start` position to `end` if the move is valid for that kind of 
        piece. We check if moves are valid.

        Args:
            match (Match): A chess match with info about the board and current
            state.
            start (str): The current position of the piece. E.g. `b3`, `d6`
            end (str): The final position of the piece.

        Raises:
            ValueError: If there is not a valid piece at `start`.
            ValueError: If `start` and `end` point to the same piece.
            ValueError: If this is an illegal move.

        Returns:
            list: The new board array after the move was made.
        """
        # TODO: Get the match from the game mode via an index.
        piece_num = board_utils.get_piece_at_pos(match.board, start)

        try:
            piece = self.get_piece_object(piece_num)
        except ValueError:
            raise ValueError("Invalid piece number.")

        if start == end:
            raise ValueError("Start and end positions match.")

        valid_moves = piece.get_valid_moves(start, match)
        if end in valid_moves:
            # Generate new board   
            new_board = match.board

            start_index = board_utils.get_board_pos_index(start)
            new_board[start_index] = 0
            end_index = board_utils.get_board_pos_index(end)
            new_board[end_index] = piece_num
            return new_board
        else:
            raise ValueError("Illegal move.")
    

    def get_piece_object(self, num):
        """Returns a piece object (e.g. King, Pawn, etc.) based on the specified 
        piece number."""
        match abs(num):
            case 1:
                return PawnPiece()
            case 2:
                return RookPiece()
            case 3:
                return KnightPiece()
            case 4:
                return BishopPiece()
            case 5:
                return QueenPiece()
            case 6:
                return KingPiece()
            case _:
                raise ValueError("Invalid piece number.")
    