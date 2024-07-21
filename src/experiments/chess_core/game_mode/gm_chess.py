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
        self.matches = []

    
    def get_initial_board(self):
        """Returns a 64-size int array that represents an 8x8 grid. Integers are used to keep track of piece types. White > 0, Black < 0.
        Note that the top left and bottom corners are light, while the top right
        and bottom left corners are dark (visually)."""
        return [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]


    def move_piece_at_pos(self, board, start, end):
        """Generates a new board array based on the movement of a particular
        piece on a given board from the start position to the end one if the 
        move is valid for that kind of piece. Throws an exception if the 
        start position has no piece, or if the move is invalid."""
        piece_num = board_utils.get_piece_at_pos(board, start)

        try:
            piece = self.get_piece_object(piece_num)
        except ValueError:
            raise ValueError("Invalid piece number.")

        valid_moves = piece.get_valid_moves(start, board)
        if end in valid_moves:
            # Generate new board   
            new_board = board

            start_index = board_utils.get_board_pos_index(start)
            new_board[start_index] = 0
            end_index = board_utils.get_board_pos_index(end)
            new_board[end_index] = piece_num
            return new_board

        else:
            raise ValueError("Invalid move.")
    

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
    