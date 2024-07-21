

from src.experiments.chess_core.pieces.p_base import BasePiece
from src.experiments.chess_core.pieces.p_bishop import BishopPiece
from src.experiments.chess_core.pieces.p_king import KingPiece
from src.experiments.chess_core.pieces.p_knight import KnightPiece
from src.experiments.chess_core.pieces.p_pawn import PawnPiece
from src.experiments.chess_core.pieces.p_queen import QueenPiece
from src.experiments.chess_core.pieces.p_rook import RookPiece


class ChessGameMode:
    """A class used to handle rules about the chess game mode."""
    def __init__(self, board=None):
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

    def get_piece_type(self, piece):
        """Converts an integer representing a chess playing piece into a string
        representation."""
        if piece > 0:
            color = "White "
        else:
            color = "Black "

        piece = abs(piece)
        match piece:
            case 1:
                return color + "Pawn"
            case 2:
                return color + "Rook"
            case 3:
                return color + "Knight"
            case 4:
                return color + "Bishop"
            case 5:
                return color + "Queen"
            case 6:
                return color + "King"
            case _:
                return "Empty"


    def get_piece_at_pos(self, board, pos):
        """Gets the piece located at a particular position on a given board."""
        index = self.get_board_pos_index(pos)
        return board[index]

        
    def get_board_pos_index(self, pos):
        """A helper function that gets the index of a particular board position
        in the 64 int board array."""
        # a -> 0, b -> 1, c -> 2
        column = ord(pos[0]) - ord('a')
        # 1 -> 7, 2 -> 6, 3 -> 5 (top is row 0)
        row = 8 - int(pos[1])
        index = column + (8 * row)
        return index
    
    
    def move_piece_at_pos(self, board, start, end):
        """Generates a new board array based on the movement of a particular
        piece on a given board from the start position to the end one if the 
        move is valid for that kind of piece. Throws an exception if the 
        start position has no piece, or if the move is invalid."""
        piece_num = self.get_piece_at_pos(board, start)

        try:
            piece = self.get_piece_object(piece_num)
        except ValueError:
            raise ValueError("Invalid piece number.")

        valid_moves = piece.get_valid_moves(start, board)
        if end in valid_moves:
            # Generate new board   
            new_board = board

            start_index = self.get_board_pos_index(start)
            new_board[start_index] = 0
            end_index = self.get_board_pos_index(end)
            new_board[end_index] = piece_num
            return new_board

        else:
            raise ValueError("Invalid move.")
    

    def get_piece_object(self, num):
        """Returns a piece object (e.g. King, Pawn, etc.) based on the specified 
        piece number."""
        is_white = (num > 0)
        match abs(num):
            case 1:
                return PawnPiece(is_white)
            case 2:
                return RookPiece(is_white)
            case 3:
                return KnightPiece(is_white)
            case 4:
                return BishopPiece(is_white)
            case 5:
                return QueenPiece(is_white)
            case 6:
                return KingPiece(is_white)
            case _:
                raise ValueError("Invalid piece number.")
    