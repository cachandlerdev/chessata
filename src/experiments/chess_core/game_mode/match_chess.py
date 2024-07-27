from src.experiments.chess_core import board_utils


class ChessMatch:
    """A class representing a chess match. Holds info about the board, pieces,
    and current state of the game."""
    
    def __init__(self, board=None, **kwargs):
        """Creates a new chess match that holds info about the board, pieces,
        and current game state.

        Args:
            board (list, optional): A 64 size int array representing the board. 
            Defaults to the initial board at the start of a chess game.

            allow_en_passant (list, optional): A 16 size boolean array used to
            keep track of whether each pawn has exposed itself to an en passant
            attack by moving two spaces on its first move. Defaults to `False`
            for each array element.
            
            has_king_moved (dict, optional): A 2 size dictionary that tracks
            whether each king has moved in the format `{6: False, -6: False}`.
            Defaults to `False` for each element.
            
            has_rook_moved (dict, optional): A 4 size dictionary that tracks
            whether each rook has moved in the format 
            `{"a1": False, "h1": False, ...}`. Defaults to `False` for each 
            element.
        """
        self.board = board if board is not None else self._get_initial_board()
        self._allow_en_passant = kwargs.get("allow_en_passant", 
                                      self._get_initial_en_passant())
        self._has_king_moved = kwargs.get("has_king_moved", 
                                    {6: False, -6: False})
        self._has_rook_moved = kwargs.get("has_rook_moved", 
                                    {"a1": False,
                                     "h1": False,
                                     "a8": False,
                                     "h8": False})
    
    
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
    
    
    def is_exposed_to_en_passant(self, piece_pos):
        """Checks whether moving a pawn from `start` to `end` via an en passant
        would be valid based on the other pawn's position, `piece_pos`.
        We assume that `piece_pos` is a valid position, and that the piece
        located there will be a valid enemy pawn.

        Args:
            start (str): The current position of the friendly pawn.
            piece_pos (str): The position of the enemy pawn to be captured.
            end (str): The final position of the friendly pawn.
        """
        is_white = board_utils.get_piece_at_pos(self.board, piece_pos) > 0
        if not self._is_farthest_back_pawn(piece_pos, is_white):
            return False

        if is_white:
            index = 8
        else:
            index = 0

        col = ord(piece_pos[0]) - ord("a")
        index += col
        
        return self._allow_en_passant[index]

    
    def _is_farthest_back_pawn(self, pos, is_white):
        """Returns true if the pawn located at this position is the farthest
        back pawn in its column."""
        if is_white:
            start_row = int(pos[1]) - 1
            for i in range(start_row, 1, -1):
                square = f"{pos[0]}{i}"
                if board_utils.get_piece_at_pos(self.board, square) == 1:
                    return False
        else:
            start_row = int(pos[1]) + 1
            for i in range(start_row, 8):
                square = f"{pos[0]}{i}"
                if board_utils.get_piece_at_pos(self.board, square) == -1:
                    return False
        return True
        