from src.experiments.chess_core.pieces.p_base import BasePiece
import src.experiments.chess_core.board_utils as board_utils


class PawnPiece(BasePiece):
    """A class representing a pawn chess piece."""
    

    def __init__(self):
        self._initial_movement_range = 2
        self._standard_movement_range = 1


    def get_valid_moves(self, start, match):
        super().get_valid_moves(start, match)
        
        moves = self._get_valid_vertical_moves(start, match, True)
        moves.extend(self._get_valid_v_moves(start, match))
        moves.extend(self._get_valid_en_passant_moves(start, match))
        
        return moves
    
    
    def _get_movement_range(self, pos, board):
        this_piece = board_utils.get_piece_at_pos(board, pos)
        if this_piece > 0:
            # White
            if int(pos[1]) == 2:
                return self._initial_movement_range
            else:
                return self._standard_movement_range
        else:
            # Black
            if int(pos[1]) == 7:
                return self._initial_movement_range
            else:
                return self._standard_movement_range
    
    
    def _get_valid_v_moves(self, start, match):
        """Returns a list of valid pawn attack V moves."""
        moves = []
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        
        if this_piece > 0:
            y = 1
        else:
            y = -1

        check_moves = []
        try:
            left = board_utils.relative_to_absolute_pos(start, (-1, y))
            check_moves.append(left)
        except ValueError:
            # Ignore invalid square.
            pass

        try:
            right = board_utils.relative_to_absolute_pos(start, (1, y))
            check_moves.append(right)
        except ValueError:
            # Ignore invalid square
            pass

        for move in check_moves:
            if board_utils.is_valid_pos(move):
                other_piece = board_utils.get_piece_at_pos(match.board, move)
                if other_piece != 0 and (
                    not board_utils.is_piece_friendly(this_piece, other_piece)
                    ):
                    moves.append(move)
        return moves
    

    def _get_valid_en_passant_moves(self, start, match):
        """Returns a list of valid en passant attack moves."""
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        moves = []
        
        if this_piece > 0:
            # White on valid row
            check_moves = (int(start[1]) == 5)
            y = 1
        else:
            # Black on valid row
            check_moves = (int(start[1]) == 4)
            y = -1
            
        if check_moves:
            # Left
            try:
                left_square = board_utils.relative_to_absolute_pos(start, (-1, 0))
                left_piece = board_utils.get_piece_at_pos(match.board, left_square)
                
                if abs(left_piece) == 1 and not (
                    board_utils.is_piece_friendly(this_piece, left_piece)):
                    end = board_utils.relative_to_absolute_pos(left_square, (0, y))
                    if match.is_exposed_to_en_passant(left_square):
                        moves.append(end)
            except ValueError:
                # This square must not exist
                pass

            # Right
            try:
                right_square = board_utils.relative_to_absolute_pos(start, (1, 0))
                right_piece = board_utils.get_piece_at_pos(match.board, right_square)

                if abs(right_piece) == 1 and not (
                    board_utils.is_piece_friendly(this_piece, right_piece)):
                    end = board_utils.relative_to_absolute_pos(right_square, (0, y))
                    if match.is_exposed_to_en_passant(right_square):
                        moves.append(end)
            except ValueError:
                # This square must not exist
                pass
        return moves
