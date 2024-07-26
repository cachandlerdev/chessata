class ChessMatch:
    """A class representing a chess match. Holds info about the board, pieces,
    and current state of the game."""
    
    def __init__(self, board=None, allow_en_passant=[]):
        if board is None:
            self.board = self._get_initial_board()
        else:
            self.board = board
        if allow_en_passant == []:
            self._allow_en_passant = self._get_initial_en_passant()
        else:
            self._allow_en_passant = allow_en_passant

    
    
    def _get_initial_board(self):
        """Returns a 64-size int array that represents an 8x8 grid. 
        Integers are used to keep track of piece types. White > 0, Black < 0.
        Note that the top left and bottom right corners are light, while the top
        right and bottom left corners are dark (visually)."""
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
    

    def _get_initial_en_passant(self):
        """This boolean array is used to check whether the pawn on this column
        has just exposed itself to an en passant attack by moving two spaces
        forward on its first move. The first 8 array elements refer to black
        pawns, while the next 8 reference white pawns.
        Note that we look at the backmost pawn in cases where multiple same 
        color pawns are located on the same column."""
        return [False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False]
    
    
    def can_perform_en_passant(self, start, end):
        pass
        