

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
        # a -> 0, b -> 1, c -> 2
        column = ord(pos[0]) - ord('a')
        # 1 -> 7, 2 -> 6, 3 -> 5 (top is row 0)
        row = 8 - int(pos[1])
        index = column + (8 * row)
        return board[index]
    
    
    def move_piece_at_pos(self, board, start, end):
        """Generates a new board array based on the movement of a particular
        piece on a given board from the start position to the end one if the 
        move is valid for that kind of piece. Throws an exception if the 
        start position has no piece, or if the move is invalid."""
        pass