def get_piece_type(piece):
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


def get_piece_at_pos(board, pos):
    """Gets the piece located at a particular position on a given board."""
    index = get_board_pos_index(pos)
    return board[index]


def get_piece_from_index(board, index):
    """Gets the piece located at a particular index on a given board."""
    pos = get_pos_from_index(index)
    return get_piece_at_pos(board, pos)

    
def get_board_pos_index(pos):
    """A helper function that gets the index of a particular board position
    in the 64 int board array."""
    # a -> 0, b -> 1, c -> 2
    column = ord(pos[0]) - ord('a')
    # 1 -> 7, 2 -> 6, 3 -> 5 (top is row 0)
    row = 8 - int(pos[1])
    index = column + (8 * row)
    return index


def is_piece_friendly(this_piece, other_piece):
    """A helper function that compares the numerical value of the two pieces
    to determine if the other piece is friendly."""
    empty_squares = (this_piece == 0) or (other_piece == 0)
    invalid_black = (this_piece < -6) or (other_piece < -6)
    invalid_white = (this_piece > 6) or (other_piece > 6)

    if empty_squares or invalid_black or invalid_white:
        raise ValueError("Invalid piece number.")
    else:
        if this_piece > 0:
            return other_piece > 0
        else:
            return other_piece < 0


def relative_to_absolute_pos(start, transform):
    """Transforms a relative position into an absolute one. 
    Eg. `a3`, `(2, 1)` -> `c4`.
    Throws a `ValueError` if the transform is invalid."""
    if not is_valid_pos(start):
        raise ValueError("Invalid starting position.")
    
    col = chr(ord(start[0]) + transform[0])
    row = int(start[1]) + transform[1]
    
    square = f"{col}{row}"
    
    if not is_valid_pos(square):
        raise ValueError("Invalid transformation.")
    
    return square


def absolute_to_relative_pos(origin, point):
    """Gets the relative transform `(x, y)` from the `origin` to the 
    destination `point`. Throws a `ValueError` if either position is invalid."""
    if not is_valid_pos(origin):
        raise ValueError("Invalid starting position.")
    if not is_valid_pos(point):
        raise ValueError("Invalid final point.")
    
    x1 = ord(origin[0]) - ord("a")
    x2 = ord(point[0]) - ord("a")
    dx = x2 - x1

    y1 = int(origin[1])
    y2 = int(point[1])
    dy = y2 - y1
    
    return (dx, dy)
    

def is_valid_pos(pos):
    """Returns true if a given position is in the range a1 through h8."""
    if len(pos) != 2:
        return False

    valid_col = (int(pos[1]) > 0) and (int(pos[1]) < 9)
    valid_row = (pos[0] >= 'a') and (pos[0] <= 'h')
    row_not_double_digits = (len(pos) == 2)
    return valid_col and valid_row and row_not_double_digits


def find_piece_pos(piece_num, board):
    """Returns the position of the first piece it finds with the specified 
    value. This is really only useful for locating the kings or queens."""
    try:
        index = board.index(piece_num)
    except ValueError:
        raise ValueError("Piece not found.")
    pos = get_pos_from_index(index)
    return pos


def get_pos_from_index(index):
    """A helper function that gets the chess board position of the specified 
    board index."""
    col = chr((index % 8) + ord("a"))
    row = 8 - (index // 8)
    return f"{col}{row}"

