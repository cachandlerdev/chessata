from src.experiments.chess_core.structs.piece_type import PieceType
from src.experiments.chess_core.structs.move_type import MoveType
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
        # TODO: Figure out how we're storing matches. Is it on the game mode?
        # A separate 'game_manager' class? Not sure.
        # I'm thinking a separate turn_manager class will be used
        self._matches = []
    

    def move_piece_at_pos(self, match, start, end, promotion_type=PieceType.QUEEN):
        """Updates the current match based on the movement of a particular piece
        from `start` position to `end` if the move is valid for that kind of 
        piece. We check if moves are valid.

        Args:
            match (Match): A chess match with info about the board and current
            state.
            start (str): The current position of the piece. E.g. `b3`, `d6`
            end (str): The final position of the piece.
            promotion_type (PieceType, optional): Used to determine what kind of
            promotion to make if we are promoting a pawn this move. Defaults to
            queen promotions.

        Raises:
            ValueError: If there is not a valid piece at `start`.
            ValueError: If `start` and `end` point to the same piece.
            ValueError: If this is an illegal move.

        Returns:
            list: The new board array after the move was made.
        """
        piece_num = board_utils.get_piece_at_pos(match.board, start)

        try:
            piece = self.get_piece_object(piece_num)
        except ValueError:
            raise ValueError("Invalid piece number.")

        if start == end:
            raise ValueError("Start and end positions match.")

        valid_moves = piece.get_valid_moves(start, match)
        # TODO: Remove all moves that would put the friendly king in check or 
        # checkmate
        # TODO: Update the match "king moved", "pawn en passant", and "rook
        # moved" states
        if end in valid_moves:
            type = self._identify_move_type(start, end, match.board)
            match type:
                case MoveType.EN_PASSANT:
                    self._update_match_en_passant(start, end, match, piece_num)
                case MoveType.PROMOTION:
                    self._update_match_promotion(start, end, match, piece_num, promotion_type)
                case MoveType.CASTLING:
                    self._update_match_castling(start, end, match, piece_num)
                case MoveType.REGULAR:
                    self._update_match_regular(start, end, match, piece_num)
        else:
            raise ValueError("Illegal move.")
    
    
    def is_in_check(self, pos, is_white, match):
        """Checks whether a king at this position for the specified match is
        in check. Note that the king doesn't actually *have* to be at this 
        position, as we're testing whether he *would* be in check if he moved 
        here."""
        if self._is_in_cross_check(pos, is_white, match):
            return True
        if self._is_in_diagonal_check(pos, is_white, match):
            return True
        if self._is_in_knight_check(pos, is_white, match):
            return True
        return False
    

    def _is_in_cross_check(self, pos, is_white, match):
        """Checks whether a king located at this position would be in check from
        rooks, queens, or the other king."""
        # TODO
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for direction in directions:
            pass
            # In each case, check whether an enemy rook, queen, or king is there
            # Only check kings for the first space away
            # If the piece is present, he's in check
        
        return False

    def _is_in_diagonal_check(self, pos, is_white, match):
        """Checks whether a king located at this position would be in check from
        bishops, queens, pawns, or the other king."""
        # TODO
        directions = [(1, -1), (1, 1), (1, -1), (-1, -1)]
        for direction in directions:
            pass
            # In each case, check whether an enemy bishop, queen, king, or pawn is 
            # there for squares in the direction
                # If a bishop or a queen, he's in check
                # Only check kings and pawns for the first space away
                # Make sure the pawns are in the right direction for attacking
                # (probably make this a separate function)
        return False

    
    def _is_in_knight_check(self, pos, is_white, match):
        """Checks whether a king located at this position would be in check from
        knights."""
        transforms = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), 
                      (-1, -2), (-2, -1)]
        for transform in transforms:
            enemy_knight = -3 if is_white else 3
            square = board_utils.relative_to_absolute_pos(pos, transform)
            square_piece = board_utils.get_piece_at_pos(match.board, square)
            if square_piece == enemy_knight:
                return True

        return False

    
    def is_in_checkmate(self, pos, is_white, match):
        """Checks whether a king at this position for the specified match is
        in checkmate."""
        # TODO
        # Get whether the piece is in check
        # If so, check whether he has any possible moves
        
        # Note: you might want to separate out the "is_in_check" logic to avoid
        # duplicating computationally intensive calculations
        return False
    
   
    def _update_match_en_passant(self, start, end, match, piece_num):
        """Updates the specified match board to account for an en passant move."""
        # TODO
        start_index = board_utils.get_board_pos_index(start)
        match.board[start_index] = 0
        end_index = board_utils.get_board_pos_index(end)
        match.board[end_index] = piece_num
        
        transform = board_utils.absolute_to_relative_pos(start, end)
        x = 1 if transform[0] > 0 else -1
        other_pawn_square = board_utils.relative_to_absolute_pos(start, (x, 0))
        other_pawn_index = board_utils.get_board_pos_index(other_pawn_square)
        match.board[other_pawn_index] = 0
    

    def _update_match_promotion(self, start, end, match, piece_num, promotion_type):
        """Updates the specified match board to account for a pawn promotion move."""
        if promotion_type == PieceType.KING or promotion_type == PieceType.PAWN:
            raise ValueError("Invalid promotion type.")
        if abs(piece_num) != 1:
            raise ValueError("Only pawns can be promoted.")
        
        start_index = board_utils.get_board_pos_index(start)
        match.board[start_index] = 0
        end_index = board_utils.get_board_pos_index(end)
        
        factor = 1 if piece_num > 0 else -1
        match.board[end_index] = factor * promotion_type.value
    
    
    def _update_match_castling(self, start, end, match, piece_num):
        """Updates the specified match board to account for a castling move."""
        # TODO
        is_white = piece_num > 0
        kingside = start[0] < end[0]
        # TODO: Making sure it's a legal move should probably be handled 
        # elsewhere
        if self._would_castling_put_king_in_check(start, kingside, is_white, match):
            raise ValueError("Illegal move.")

        if kingside:
            new_rook_pos = board_utils.relative_to_absolute_pos(start, (1, 0))
            new_king_pos = board_utils.relative_to_absolute_pos(start, (2, 0))
            old_rook_pos = f"h{start[1]}"
        else:
            new_rook_pos = board_utils.relative_to_absolute_pos(start, (-1, 0))
            new_king_pos = board_utils.relative_to_absolute_pos(start, (-2, 0))
            old_rook_pos = f"a{start[1]}"
        
        old_rook_index = board_utils.get_board_pos_index(old_rook_pos)
        old_king_index = board_utils.get_board_pos_index(start)
        new_rook_index = board_utils.get_board_pos_index(new_rook_pos)
        new_king_index = board_utils.get_board_pos_index(new_king_pos)

        rook_value = match.board[old_rook_index]
        match.board[old_rook_index] = 0
        match.board[old_king_index] = 0
        match.board[new_rook_index] = rook_value
        match.board[new_king_index] = piece_num
    
    
    def _would_castling_put_king_in_check(self, start, kingside, is_white, match):
        """Returns true if castling would put the king in check."""
        dx = 1 if kingside else -1
        squares_to_check = []
        square1 = board_utils.relative_to_absolute_pos(start, (dx * 1, 0))
        square2 = board_utils.relative_to_absolute_pos(start, (dx * 2, 0))
        squares_to_check.append(square1)
        squares_to_check.append(square2)

        for square in squares_to_check:
            if self.is_in_check(square, is_white, match):
                return True
        return False
 

    def _update_match_regular(self, start, end, match, piece_num):
        """Updates the specified match board to account for a regular move."""
        start_index = board_utils.get_board_pos_index(start)
        match.board[start_index] = 0
        end_index = board_utils.get_board_pos_index(end)
        match.board[end_index] = piece_num
    

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
    

    def _identify_move_type(self, start, end, board):
        """Tries to identify the type of move that was just made. The special 
        move types we look for are en passants, pawn promotions, and castling.
        If it wasn't one of these, we assume it was a regular move."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        
        if abs(this_piece) == 1:
            if self._is_pawn_promotion_move(start, end, this_piece):
                return MoveType.PROMOTION
            if self._is_en_passant_move(start, end, board, this_piece):
                return MoveType.EN_PASSANT
        elif abs(this_piece) == 6:
            if self._is_castling_move(start, end, board, this_piece):
                return MoveType.CASTLING
        
        return MoveType.REGULAR

    
    def _is_en_passant_move(self, start, end, board, this_piece):
        """Returns true if this was an en passsant move."""
        if this_piece > 0:
            y = 1
        else:
            y = -1
        
        transform = board_utils.absolute_to_relative_pos(start, end)
        is_left_attack = (transform[0] == -1) and (transform[1] == y)
        is_right_attack = (transform[0] == 1) and (transform[1] == y)
        
        if is_left_attack:
            left_square = board_utils.relative_to_absolute_pos(start, (-1, 0))
            square_piece = board_utils.get_piece_at_pos(board, left_square)
            if (abs(square_piece) == 1) and not (
                board_utils.is_piece_friendly(this_piece, square_piece)):
                return True
        
        if is_right_attack:
            right_square = board_utils.relative_to_absolute_pos(start, (1, 0))
            square_piece = board_utils.get_piece_at_pos(board, right_square)
            if (abs(square_piece) == 1) and not (
                board_utils.is_piece_friendly(this_piece, square_piece)):
                return True

        return False
 

    def _is_pawn_promotion_move(self, start, end, this_piece):
        """Returns true if this was a pawn promotion move."""
        if abs(this_piece) != 1:
            return False

        if this_piece > 0:
            right_start = (int(start[1]) == 7)
            right_end = (int(end[1]) == 8)
            return right_start and right_end
        else:
            right_start = (int(start[1]) == 2)
            right_end = (int(end[1]) == 1)
            return right_start and right_end


    def _is_castling_move(self, start, end, board, this_piece):
        """Returns true if this was a castling move. We assume the piece at the
        start position was a king."""
        # TODO
        if this_piece > 0:
            right_row = (int(start[1]) == 1)
        else:
            right_row = (int(start[1]) == 8)
        
        stay_on_row = (start[1] == end[1])

        move_length = abs(ord(start[0]) - ord(end[0]))
        right_length = (move_length == 2)
        
        return right_row and stay_on_row and right_length
