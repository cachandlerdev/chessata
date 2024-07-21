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

    
def get_board_pos_index(pos):
    """A helper function that gets the index of a particular board position
    in the 64 int board array."""
    # a -> 0, b -> 1, c -> 2
    column = ord(pos[0]) - ord('a')
    # 1 -> 7, 2 -> 6, 3 -> 5 (top is row 0)
    row = 8 - int(pos[1])
    index = column + (8 * row)
    return index