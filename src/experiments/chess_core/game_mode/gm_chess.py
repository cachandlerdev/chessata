from src.experiments.chess_core.structs.piece_type import PieceType
from src.experiments.chess_core.structs.move_type import MoveType
from src.experiments.chess_core.pieces.p_bishop import BishopPiece
from src.experiments.chess_core.pieces.p_king import KingPiece
from src.experiments.chess_core.pieces.p_knight import KnightPiece
from src.experiments.chess_core.pieces.p_pawn import PawnPiece
from src.experiments.chess_core.pieces.p_queen import QueenPiece
from src.experiments.chess_core.pieces.p_rook import RookPiece
import src.experiments.chess_core.board_utils as board_utils
import copy


class ChessGameMode:
    """A class used to handle rules about the chess game mode."""

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

        moves = piece.get_valid_moves(start, match)
        moves = self._remove_friendly_check_moves(moves, start, promotion_type, match)
        # TODO: Update the match "king moved", "pawn en passant", and "rook
        # moved" states
        if end in moves:
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
    
    
    def resolve_game_state(self, match, is_white_turn):
        """Determines whether the specified match is over yet. Returns 0 if the
        game is not over yet, 1 if the white player is in check, 2 if the black 
        player is in check, 3 if the game ended in a stalemate, 4 if the white 
        player has won, and 5 if the black player has won."""
        # TODO
        # Is white player in check?
            # Does white player not have moves?
                # Checkmate. Black wins
                # return 4
            # else
                # Check for white.
                # return 1
        
        # Is black player in check?
            # Does black player not have moves?
                # Checkmate. White wins
                # return 4
            # else
                # Check for black
                # return 2
        
        # Does current player have moves?
            # Game's not over yet
            # return 0
        # else:
            # Stalemate
            # return 3
        return 0
    
    
    # TODO Handle limiting player moves if the current player is in check
    
    
    def _remove_friendly_check_moves(self, all_moves, start, promotion_type, match):
        """Removes all moves that would put the friendly king in check and 
        returns the resulting moves."""
        piece_to_move = board_utils.get_piece_at_pos(match.board, start)
        check_white_king = (piece_to_move > 0)
        valid_moves = []
        
        for move in all_moves:
            type = self._identify_move_type(start, move, match.board)
            invalid_castling = (type == MoveType.CASTLING) and (
                self._is_illegal_castling_move(start, move, check_white_king, match))
            invalid_regular = self._is_illegal_regular_move(start, move, check_white_king, type, promotion_type, match)
            if not invalid_castling and not invalid_regular:
                valid_moves.append(move)
        return valid_moves
    

    def _is_illegal_regular_move(self, start, end, check_white_king, move_type, promotion_type, match):
        """Checks whether making this move would put the friendly king in check,
        and therefore be an illegal move. Note that this function does not
        handle castling cases."""
        # TODO
        new_match = copy.deepcopy(match)
        this_piece = board_utils.get_piece_at_pos(new_match.board, start)
        match move_type:
            case MoveType.EN_PASSANT:
                self._update_match_en_passant(start, end, new_match, this_piece)
            case MoveType.PROMOTION:
                self._update_match_promotion(start, end, new_match, this_piece, promotion_type)
            case MoveType.REGULAR:
                self._update_match_regular(start, end, new_match, this_piece)

        king_value = 6 if check_white_king else -6
        king_pos = board_utils.find_piece_pos(king_value, new_match.board)
        return self.is_in_check(king_pos, check_white_king, new_match)
    
    
    def _is_illegal_castling_move(self, start, end, check_white_king, match):
        """Looks at whether making this castling move would be legal with regard 
        to check rules. Namely, we determine whether the king is trying to 
        castle out of, through, or into check."""
        x = 1 if start[0] < end[0] else -1
        if self.is_in_check(start, check_white_king, match):
            # Castle out of check
            return True

        middle = board_utils.relative_to_absolute_pos(start, (x, 0))
        if self.is_in_check(middle, check_white_king, match):
            # Castle through check
            return True
        
        if self.is_in_check(end, check_white_king, match):
            # Castle into check
            return True
        
        return False
    
    
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
        if is_white:
            enemy_pieces = [-2, -5, -6]
        else:
            enemy_pieces = [2, 5, 6]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for direction in directions:
            if self._is_in_directional_check(pos, is_white, direction, 
                                             enemy_pieces, match.board):
                return True
        return False


    def _is_in_diagonal_check(self, pos, is_white, match):
        """Checks whether a king located at this position would be in check from
        bishops, queens, pawns, or the other king."""
        if is_white:
            enemy_pieces = [-1, -4, -5, -6]
        else:
            enemy_pieces = [1, 4, 5, 6]
        
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        for direction in directions:
            if self._is_in_directional_check(pos, is_white, direction, 
                                             enemy_pieces, match.board):
                return True
        return False

    def _is_in_directional_check(self, pos, is_white, direction, enemy_pieces, board):
        """Checks whether a king located at this position would be in check
        for the specified list of enemy pieces in the given direction.
        Note: You must specify whether the enemy pieces are white or black by
        inputting positive/negative piece numbers!"""
        square = pos
        distance = 0
        while (square[0] >= "a" and square[0] <= "h") and (
            int(square[1]) >= 1 and int(square[1]) <= 8):
            try:
                new_square = board_utils.relative_to_absolute_pos(square, direction)
            except ValueError:
                # We've reached the edge of the board
                return False

            distance += 1
            square_piece = board_utils.get_piece_at_pos(board, new_square)
            if square_piece != 0:
                if square_piece in enemy_pieces:
                    match abs(square_piece):
                        # Pawn
                        case 1:
                            right_distance = (distance == 1)
                            y_to_check = 1 if is_white else -1
                            right_direction = direction[1] == y_to_check
                            return right_distance and right_direction
                        # King
                        case 6:
                            return (distance == 1)
                        # Others
                        case _:
                            return True
                # Even if he's not in check, we still stop looking in this 
                # direction because we found the first piece in this direction.
                return False
            square = new_square
        # Checked all squares in this direction
        return False

    
    def _is_in_knight_check(self, pos, is_white, match):
        """Checks whether a king located at this position would be in check from
        knights."""
        transforms = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), 
                      (-1, -2), (-2, -1)]
        for transform in transforms:
            enemy_knight = -3 if is_white else 3
            try:
                square = board_utils.relative_to_absolute_pos(pos, transform)
            except ValueError:
                # This square doesn't exist
                continue
            square_piece = board_utils.get_piece_at_pos(match.board, square)
            if square_piece == enemy_knight:
                return True

        return False

    
    #def is_in_checkmate(self, pos, is_white, match):
    #    """Checks whether a king at this position for the specified match is
    #    in checkmate."""
    #    # TODO
    #    if not self.is_in_check(pos, is_white, match):
    #        return False
    #    
    #    king = KingPiece()
    #    moves = king.get_valid_moves(pos, match)
    #    moves = self._remove_friendly_check_moves(moves, pos, promotion_type, match)
    #    return len(moves) == 0
    #    # Note: you might want to separate out the "is_in_check" logic to avoid
    #    # duplicating computationally intensive calculations
    #    return False
    
   
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
