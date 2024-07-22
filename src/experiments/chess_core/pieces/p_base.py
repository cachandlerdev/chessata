import src.experiments.chess_core.board_utils as board_utils


class BasePiece:
    """The base class for all chess pieces."""
    
    def __init__(self, movement_type="+XL|", movement_range=[8], attack_type=""):
        """Creates a new chess piece.

        Args:
            movement_type (str): The kind of movement allowed for this
            piece when not attacking. Valid movement options are "+, X, L, |".
            movement_range (list): A list that represents the number 
            of squares this piece can move. Regular pieces will have one element
            (e.g. king -> [1], queen -> [8]). Pawns should be [1, 2] to reflect
            their move distance on the first play. This property is not used for 
            knights.
            attack_type (str, optional): Only set this on pawns, since their 
            attack movement differs from their regular movement. Describes the
            kind of movement allowed for this piece when not attacking. Valid 
            movement options are "+, X, L, |, V". (Only "V" gets used though.)
        """
        self.movement_type = movement_type
        self.movement_range = movement_range

        if attack_type == "":
            self.attack_type = self.movement_type
        else:
            self.attack_type = attack_type
    
    def get_valid_moves(self, start, board):
        """Returns a list of valid moves for this piece based on the specified
        board and start position."""
        # TODO: Add king check based on movement
        # TODO: Make sure pieces stay on the board (probably a helper function on this class that gets used by subclasses)
        raise NotImplementedError("Handled by children.")
    
    
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
            movement_rules = self.attack_type
        else:
            movement_rules = self.movement_type
        
        movement_type_used = self.get_movement_type_used(start, end, movement_rules)

        match movement_type_used:
            case "|":
                return self.does_vertical_move_collide(start, end, board)
            case "+":
                return self.does_plus_move_collide(start, end, board)
            case "X" | "V":
                return self.does_diagonal_move_collide(start, end, board)
            case _:
                return self.does_L_move_collide(this_piece, target_pos)
    
    
    def get_movement_type_used(self, start, end, movement_rules):
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
    
    
    def does_vertical_move_collide(self, start, end, board):
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
    

    def does_plus_move_collide(self, start, end, board):
        """Checks whether there is a vertical or a horizontal collision for the
        specified move. Returns 0 if it doesn't collide, 1 if it collides with 
        an enemy, and 2 if it collides with a friendly."""
        if start[0] == end[0]:
            # Vertical move
            return self.does_vertical_move_collide(start, end, board)

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


    def does_diagonal_move_collide(self, start, end, board):
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


    def does_L_move_collide(self, this_piece, target_pos):
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
    
