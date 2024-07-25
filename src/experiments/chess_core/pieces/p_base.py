import src.experiments.chess_core.board_utils as board_utils


class BasePiece:
    """The base class for all chess pieces."""
    
    def __init__(self, movement_type="+XL|V", movement_range=[8], attack_type=""):
        """Creates a new chess piece.

        Args:
            _movement_type (str): The kind of movement allowed for this
            piece when not attacking. Valid movement options are "+, X, L, |".
            _movement_range (list): A list that represents the number 
            of squares this piece can move. Regular pieces will have one element
            (e.g. king -> [1], queen -> [8]). Pawns should be [1, 2] to reflect
            their move distance on the first play. This property is not used for 
            knights.
            _attack_type (str, optional): Only set this on pawns, since their 
            attack movement differs from their regular movement. Describes the
            kind of movement allowed for this piece when not attacking. Valid 
            movement options are "+, X, L, |, V". (Only "V" gets used though.)
        """
        self._movement_type = movement_type
        self._movement_range = movement_range

        if attack_type == "":
            self._attack_type = self._movement_type
        else:
            self._attack_type = attack_type
    
    def get_valid_moves(self, start, board):
        """Returns a list of valid moves for this piece based on the specified
        board and start position."""
        # TODO: Add king check based on movement
        
        this_piece = board_utils.get_piece_at_pos(board, start)
        if this_piece == 0:
            raise ValueError("Piece not found.")
        
        # Pawns can only move forward
        if self._movement_type == "|":
            forward_only = True
        else:
            forward_only = False

        moves = []
        for type in self._movement_type:
            match type:
                case "|":
                    moves.extend(self._get_valid_vertical_moves(start, board, "|", forward_only))
                case "+":
                    moves.extend(self._get_valid_cross_moves(start, board))
                case "X":
                    moves.extend(self._get_valid_diagonal_moves(start, board))
                case "V":
                    moves.extend(self._get_valid_v_moves(start, board))
                case _:
                    moves.extend(self._get_valid_L_moves(start, board))

        return moves
    
    
    def _get__movement_range(self, pos, board):
        """Gets the movement range of this particular piece."""
        # TODO: Add special behavior for pawns on the PawnPiece class
        return self._movement_range[0]

    
    def _get_valid_vertical_moves(self, start, board, move_type, forward_only):
        """Returns a list of valid vertical move positions for this piece based
        on the specified board and start position."""
        moves = []
        col = start[0]
        row = int(start[1])
        
        this_piece = board_utils.get_piece_at_pos(board, start)
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
            max_range = min(row + self._get__movement_range(start, board) + 1, 9)
            for i in range(row + 1, max_range):
                square = f"{col}{i}"
                found_collision = self.__add_move_if_valid(start, square, board, moves, move_type)
                if found_collision:
                    break
        
        if check_below:
            # Check square below
            min_range = max(row - self._get__movement_range(start, board) - 1, 0)
            for i in range(row - 1, min_range, -1):
                square = f"{col}{i}"
                found_collision = self.__add_move_if_valid(start, square, board, moves, move_type)
                if found_collision:
                    break

        return moves
    
    
    def __add_move_if_valid(self, start, end, board, moves, move_type):
        """Checks whether this move can be added by looking for piece collision
        and adds it if possible. Returns true if there was a collision."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        square_piece = board_utils.get_piece_at_pos(board, end)
        if square_piece != 0:
            # Collision found
            if not board_utils.is_piece_friendly(this_piece, square_piece):
                if move_type in self._attack_type:
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
    
    
    def _get_valid_cross_moves(self, start, board):
        """Returns a list of valid horizontal and vertical move positions for
        this piece based on the specified board and start position."""
        moves = []
        # Get vertical moves
        moves.extend(self._get_valid_vertical_moves(start, board, "+", False))
        
        col = start[0]
        row = int(start[1])

        # Check squares left
        min_range = max(chr(ord(col) - self._get__movement_range(start, board)), "a")
        for c in self.__char_range(chr(ord(col) - 1), min_range, -1):
            square = f"{c}{row}"
            found_collision = self.__add_move_if_valid(start, square, board, moves, "+")
            if found_collision:
                break
        
        # Check squares right
        max_range = min(chr(ord(col) + self._get__movement_range(start, board)), "h")
        for c in self.__char_range(chr(ord(col) + 1), max_range):
            square = f"{c}{row}"
            found_collision = self.__add_move_if_valid(start, square, board, moves, "+")
            if found_collision:
                break

        return moves

    
    def _get_valid_diagonal_moves(self, start, board):
        """Returns a list of valid diagonal move positions for this piece based
        on the specified board and start position."""
        moves = []
        
        top_left = self._get_diagonal_end(start, -1, 1, board)
        self.__get_diagonal_move_subset(start, top_left, board, moves)
        
        top_right = self._get_diagonal_end(start, 1, 1, board)
        self.__get_diagonal_move_subset(start, top_right, board, moves)
        
        bottom_left = self._get_diagonal_end(start, -1, -1, board)
        self.__get_diagonal_move_subset(start, bottom_left, board, moves)
        
        bottom_right = self._get_diagonal_end(start, 1, -1, board)
        self.__get_diagonal_move_subset(start, bottom_right, board, moves)
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

        if not self._is_valid_pos(start):
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
            if spaces_traversed > self._get__movement_range(start, board):
                break
        return prev_pos
    

    def _get_valid_v_moves(self, start, board):
        """Returns a list of valid pawn attack V moves."""
        # TODO: Handle en passant moves on pawn class

        moves = []
        this_piece = board_utils.get_piece_at_pos(board, start)
        
        if this_piece > 0:
            y = 1
        else:
            y = -1

        left = f"{chr(ord(start[0]) - 1)}{int(start[1]) + y}"
        right = f"{chr(ord(start[0]) + 1)}{int(start[1]) + y}"
        check_moves = [left, right]
        for move in check_moves:
            if self._is_valid_pos(move):
                other_piece = board_utils.get_piece_at_pos(board, move)
                if other_piece != 0 and (
                    not board_utils.is_piece_friendly(this_piece, other_piece)
                    ):
                    moves.append(move)
        return moves
                    
    
    def _get_valid_L_moves(self, start, board):
        """Returns a list of valid L move positions for this piece based on
        the specified board and start position."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        transforms = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), 
                          (-1, -2), (-2, -1)]
        valid_moves = []
        
        for transform in transforms:
            try:
                square = self._relative_to_absolute_pos(start, transform)
                square_piece = board_utils.get_piece_at_pos(board, square)
                if square_piece == 0:
                    valid_moves.append(square)
                else:
                    if not board_utils.is_piece_friendly(this_piece, square_piece):
                        valid_moves.append(square)
            except ValueError:
                # Skip this invalid move
                continue
            
        return valid_moves
    
    
    def _relative_to_absolute_pos(self, start, transform):
        """Transforms a relative position into an absolute one. 
        Eg. `a3`, `(2, 1)` -> `c4`.
        Throws a `ValueError` if the transform is invalid."""
        if not self._is_valid_pos(start):
            raise ValueError("Invalid starting position.")
        
        col = chr(ord(start[0]) + transform[0])
        row = int(start[1]) + transform[1]
        
        square = f"{col}{row}"
        
        if not self._is_valid_pos(square):
            raise ValueError("Invalid transformation.")
        
        return square
    
    
    def does_move_collide(self, start, end, board):
        """A helper method used on children to determine if the given move will 
        collide with another piece. Returns 0 if it doesn't collide, 1 if it 
        collides with an enemy, and 2 if it collides with a friendly. We use the 
        attack type if the end position has an enemy piece.
        Note: We assume that this move is possible."""
        if start == end:
            raise ValueError("Start and end positions match.")

        this_piece = board_utils.get_piece_at_pos(board, start)
        target_pos = board_utils.get_piece_at_pos(board, end)
        
        if this_piece == 0:
            raise ValueError("No piece at start position.")
        
        if this_piece > 0:
            use_attack_movement = (target_pos < 0)
        else:
            use_attack_movement = (target_pos > 0)
        
        # Look at the movement type
        if use_attack_movement:
            movement_rules = self._attack_type
        else:
            movement_rules = self._movement_type
        
        _movement_type_used = self._get__movement_type_used(start, end, movement_rules)

        match _movement_type_used:
            case "|":
                return self.__does_vertical_move_collide(start, end, board)
            case "+":
                return self.__does_plus_move_collide(start, end, board)
            case "X" | "V":
                return self.__does_diagonal_move_collide(start, end, board)
            case _:
                return self.__does_L_move_collide(this_piece, target_pos)
    
    
    def _get__movement_type_used(self, start, end, movement_rules):
        """A helper function used to determine what kind of movement should be
        used to move from point A to point B, based on the provided movement 
        rules. Returns a movement type like '|', '+', etc."""
        if movement_rules == "":
            raise ValueError("No movement type specified.")

        if len(movement_rules) == 1:
            return movement_rules
        else:
            if (start[0] == end[0]) or (start[1] == end[1]):
                return "+"
            else:
                return "X"
    
    
    def __does_vertical_move_collide(self, start, end, board):
        """Checks whether there is a vertical collision for the specified move.
        Returns 0 if it doesn't collide, 1 if it collides with an enemy, and 2 
        if it collides with a friendly."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        if start[1] < end[1]:
            # Going up
            step = 1
        else:
            # Going down
            step = -1
        for i in range(int(start[1]) + step, int(end[1]) + step, step):
            square = f"{start[0]}{i}"
            square_piece = board_utils.get_piece_at_pos(board, square)
            if square_piece != 0:
                # Collision found
                if board_utils.is_piece_friendly(this_piece, square_piece):
                    return 2
                else:
                    return 1
        return 0
    

    def __does_plus_move_collide(self, start, end, board):
        """Checks whether there is a vertical or a horizontal collision for the
        specified move. Returns 0 if it doesn't collide, 1 if it collides with 
        an enemy, and 2 if it collides with a friendly."""
        if start[0] == end[0]:
            # Vertical move
            return self.__does_vertical_move_collide(start, end, board)

        this_piece = board_utils.get_piece_at_pos(board, start)
        if start[0] < end[0]:
            # Going right
            step = 1
        else:
            # Going down
            step = -1
        
        start_index = ord(start[0]) - ord('a')
        end_index = ord(end[0]) - ord('a')
        for i in range(start_index + step, end_index + step, step):
            column = chr(i + ord('a'))
            square = f"{column}{start[1]}"
            square_piece = board_utils.get_piece_at_pos(board, square)
            if square_piece != 0:
                if board_utils.is_piece_friendly(this_piece, square_piece):
                    return 2
                else:
                    return 1
        return 0


    def __does_diagonal_move_collide(self, start, end, board):
        """Checks whether there is a diagonal collision for the specified 
        move. Returns 0 if it doesn't collide, 1 if it collides with an enemy, 
        and 2 if it collides with a friendly."""
        this_piece = board_utils.get_piece_at_pos(board, start)

               
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
            square_piece = board_utils.get_piece_at_pos(board, square)
            if square_piece != 0:
                if board_utils.is_piece_friendly(this_piece, square_piece):
                    return 2
                else:
                    return 1
        return 0


    def __does_L_move_collide(self, this_piece, target_pos):
        """Checks whether there is a collision for an L move at the specified 
        target point. Returns 0 if it doesn't collide, 1 if it collides with an
        enemy, and 2 if it collides with a friendly."""
        if this_piece > 0:
            # White piece
            if target_pos < 0:
                return 1
            elif target_pos > 0:
                return 2
            else:
                return 0
        else:
            # Black piece
            if target_pos > 0:
                return 1
            elif target_pos < 0:
                return 2
            else:
                return 0
            
    
    def _is_valid_pos(self, pos):
        """A helper function that returns whether a given position is in the
        range a1 through h8."""
        valid_col = (int(pos[1]) > 0) and (int(pos[1]) < 9)
        valid_row = (pos[0] >= 'a') and (pos[0] <= 'h')
        row_not_double_digits = (len(pos) == 2)
        return valid_col and valid_row and row_not_double_digits
    
