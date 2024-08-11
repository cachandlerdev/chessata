from .. import board_utils


class BasePiece:
    """The base class for all chess pieces."""
    
    def __init__(self, movement_range=8):
        """Creates a new chess piece.

        Args:
            _movement_range (int): The number of squares this piece can move.
            This property is not used for knights or pawns.
        """
        self._movement_range = movement_range

    
    def get_valid_moves(self, start, match):
        """Returns a list of valid moves for this piece based on the specified
        board and start position. Note that this function does not check whether
        the moves will put the friendly king in check. That logic is handled on
        the gamemode class.

        Args:
            start (str): The initial position for this piece. E.g. `a1`, `g4`.
            match (Match): The current chess match.

        Raises:
            ValueError: This will show if `start` does not have a valid piece.

        Returns:
            list: A list of valid positions like `b3`, `e6`, and `f2`.
        """
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        if this_piece == 0:
            raise ValueError("Piece not found.")
    
    
    def _get_movement_range(self, pos, board):
        """Gets the movement range of this particular piece."""
        return self._movement_range

    
    def _get_valid_vertical_moves(self, start, match, forward_only):
        """Returns a list of valid vertical move positions for this piece based
        on the specified board and start position."""
        moves = []
        col = start[0]
        row = int(start[1])
        
        # Only pawns can't attack straight
        can_attack = not forward_only
        
        this_piece = board_utils.get_piece_at_pos(match.board, start)
        if forward_only:
            if this_piece > 0:
                # White
                check_above = True
                check_below = False
            else:
                # Black
                check_above = False
                check_below = True
        else:
            check_above = True
            check_below = True

        if check_above:
            # Check squares above
            max_range = min(row + self._get_movement_range(start, match.board) + 1, 9)
            for i in range(row + 1, max_range):
                square = f"{col}{i}"
                found_collision = self.__add_move_if_valid(start, square, match.board, moves, can_attack)
                if found_collision:
                    break
        
        if check_below:
            # Check square below
            min_range = max(row - self._get_movement_range(start, match.board) - 1, 0)
            for i in range(row - 1, min_range, -1):
                square = f"{col}{i}"
                found_collision = self.__add_move_if_valid(start, square, match.board, moves, can_attack)
                if found_collision:
                    break

        return moves
    
    
    def __add_move_if_valid(self, start, end, board, moves, can_attack):
        """Checks whether this move can be added by looking for piece collision
        and adds it if possible. Returns true if there was a collision."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        square_piece = board_utils.get_piece_at_pos(board, end)
        if square_piece != 0:
            # Collision found
            if not board_utils.is_piece_friendly(this_piece, square_piece):
                if can_attack:
                    moves.append(end)
            return True
        else:
            # No collision
            moves.append(end)
            return False
    
    
    def __char_range(self, c1, c2, step=1):
        """Generates the characters from `c1` to `c2`, inclusive."""
        end = ord(c2) + (1 if step > 0 else -1)
        for c in range(ord(c1), end, step):
            yield chr(c)
    
    
    def _get_valid_cross_moves(self, start, match):
        """Returns a list of valid horizontal and vertical move positions for
        this piece based on the specified match and start position."""
        moves = []
        # Get vertical moves
        moves.extend(self._get_valid_vertical_moves(start, match, False))
        
        col = start[0]
        row = int(start[1])

        # Check squares left
        min_range = max(chr(ord(col) - self._get_movement_range(start, match.board)), "a")
        for c in self.__char_range(chr(ord(col) - 1), min_range, -1):
            square = f"{c}{row}"
            found_collision = self.__add_move_if_valid(start, square, match.board, moves, True)
            if found_collision:
                break
        
        # Check squares right
        max_range = min(chr(ord(col) + self._get_movement_range(start, match.board)), "h")
        for c in self.__char_range(chr(ord(col) + 1), max_range):
            square = f"{c}{row}"
            found_collision = self.__add_move_if_valid(start, square, match.board, moves, True)
            if found_collision:
                break

        return moves

    
    def _get_valid_diagonal_moves(self, start, match):
        """Returns a list of valid diagonal move positions for this piece based
        on the specified match and start position."""
        moves = []
        
        top_left = self._get_diagonal_end(start, -1, 1, match.board)
        self.__get_diagonal_move_subset(start, top_left, match.board, moves)
        
        top_right = self._get_diagonal_end(start, 1, 1, match.board)
        self.__get_diagonal_move_subset(start, top_right, match.board, moves)
        
        bottom_left = self._get_diagonal_end(start, -1, -1, match.board)
        self.__get_diagonal_move_subset(start, bottom_left, match.board, moves)
        
        bottom_right = self._get_diagonal_end(start, 1, -1, match.board)
        self.__get_diagonal_move_subset(start, bottom_right, match.board, moves)
        return moves

    
    def __get_diagonal_move_subset(self, start, end, board, moves):
        """Appends the valid diagonal move positions from the starting place in the 
        direction of the end one to the moves list."""
        if start[0] < end[0]:
            h_step = 1
        else:
            h_step = -1
        
        if start[1] < end[1]:
            v_step = 1
        else:
            v_step = -1

        square = start

        while (square[0] != end[0]) and (square[0] != end[1]):
            col = chr(ord(square[0]) + h_step)
            row = int(square[1]) + v_step
            square = f"{col}{row}"
            found_collision = self.__add_move_if_valid(start, square, board, moves, "X")
            if found_collision:
                break
        return moves


    def _get_diagonal_end(self, start, x, y, board):
        """A helper function that gets the last chess square diagonally relative
        to the start position. `x` and `y` specify the direction. E.g. Up-right 
        is x=1, y=1, Up-left is x=-1, y=1, etc."""
        if (abs(x) != 1) or (abs(y) != 1):
            raise ValueError("Invalid direction.")

        if not board_utils.is_valid_pos(start):
            raise ValueError("Invalid starting position.")
        
        square = start
        prev_pos = square
        
        spaces_traversed = 0
        while (square[0] >= "a" and square[0] <= "h") and (
            int(square[1]) >= 1 and int(square[1]) <= 8
            ):
            prev_pos = square
            col = chr(ord(square[0]) + x)
            row = int(square[1]) + y
            square = f"{col}{row}"

            spaces_traversed += 1
            if spaces_traversed > self._get_movement_range(start, board):
                break
        return prev_pos
