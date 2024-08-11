from .. import board_utils
from .p_base import BasePiece


class KingPiece(BasePiece):
    """A class representing a king chess piece."""
    
    def __init__(self):
        """Creates a king object."""
        self._movement_range = 1


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        moves = self._get_valid_cross_moves(start, match)
        moves.extend(self._get_valid_diagonal_moves(start, match))
        moves.extend(self._get_valid_castling_moves(start, match))
        return moves
    
    
    def _get_valid_castling_moves(self, start, match):
        """Gets the valid castling moves for this king piece."""
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        is_white = this_piece > 0
        if match.has_king_moved(is_white):
            return []
        
        moves = []
        queenside_check = not match.has_rook_moved(is_white, False)
        kingside_check = not match.has_rook_moved(is_white, True)
        
        if queenside_check:
            if self._is_castling_path_clear(start, False, match):
                move = board_utils.relative_to_absolute_pos(start, (-2, 0))
                moves.append(move)
        
        if kingside_check:
            if self._is_castling_path_clear(start, True, match):
                move = board_utils.relative_to_absolute_pos(start, (2, 0))
                moves.append(move)
        return moves

    
    def _is_castling_path_clear(self, start, is_kingside, match):
        """Returns true if the castling route is clear in this direction."""
        if is_kingside:
            square1 = board_utils.relative_to_absolute_pos(start, (1, 0))
            square2 = board_utils.relative_to_absolute_pos(start, (2, 0))
            piece1 = board_utils.get_piece_at_pos(match.board, square1)
            piece2 = board_utils.get_piece_at_pos(match.board, square2)
            clear1 = piece1 == 0
            clear2 = piece2 == 0
            return clear1 and clear2
        else:
            square1 = board_utils.relative_to_absolute_pos(start, (-1, 0))
            square2 = board_utils.relative_to_absolute_pos(start, (-2, 0))
            square3 = board_utils.relative_to_absolute_pos(start, (-3, 0))
            piece1 = board_utils.get_piece_at_pos(match.board, square1)
            piece2 = board_utils.get_piece_at_pos(match.board, square2)
            piece3 = board_utils.get_piece_at_pos(match.board, square3)
            clear1 = piece1 == 0
            clear2 = piece2 == 0
            clear3 = piece3 == 0
            return clear1 and clear2 and clear3
            
    
