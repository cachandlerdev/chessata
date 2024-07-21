import src.experiments.chess_core.board_utils as board_utils


class BasePiece:
    """The base class for all chess pieces."""
    
    def __init__(self, movement_type="Any", movement_range=[8], attack_type=""):
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
        attack type if the end position has an enemy piece."""
        this_piece = board_utils.get_piece_at_pos(board, start)
        target_pos = board_utils.get_piece_at_pos(board, end)
        
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

        if movement_type_used == "|":
            return self.does_vertical_move_collide(start, end, board)
        elif movement_type_used == "+":
            return self.does_plus_move_collide(start, end, board)
        elif movement_type_used == "X":
            return self.does_diagonal_move_collide(start, end, board)
        elif movement_type_used == "V":
            return self.does_v_move_collide(start, end, board)
        else:
            return self.does_L_move_collide(this_piece, target_pos)
    
    
    def get_movement_type_used(self, start, end, movement_rules):
        """A helper function used to determine what kind of movement should be
        used to move from point A to point B, based on the provided movement 
        rules."""
        pass
    
    
    def does_vertical_move_collide(self, start, end, board):
        """Checks whether there is a vertical collision for the specified move."""
        #if ... start end:
        #    # Going up
        #    ... start 
        #    ... end
        #    ... board
        #else:
        #    # Going down
        #    ... start
        #    ... end
        #    ... board
        pass
    

    def does_plus_move_collide(self, start, end, board):
        """Checks whether there is a vertical or a horizontal collision for the
        specified move."""
        # Could probably incorporate the vertical move check here
        #if ... start end:
        #    # Going up
        #    ... start
        #    ... end
        #    ... board
        #elif ... start end:
        #    # Going down
        #    ... start
        #    ... end
        #    ... board
        #elif ... start end:
        #    # Going left
        #    ... start
        #    ... end
        #    ... board
        #else:
        #    # Going right
        #    ... start
        #    ... end
        #    ... board
        pass


    def does_v_move_collide(self, start, end, board):
        """Checks whether there is an upper diagonal collision for the specified 
        move."""
        # Maybe refactor later to have a boolean "going up" or "going down" var
        # so you don't need to do the same thing again for the diagonal move.
        #if ... start end:
        #    # Going up right
        #    ... start
        #    ... end
        #    ... board
        #else:
        #    # Going up left
        #    ... start
        #    ... end
        #    ... board

    
    def does_diagonal_move_collide(self, start, end, board):
        """Checks whether there is a diagonal collision for the specified move."""
        # Could probably incorporate V check here
        #if ... start end:
        #    # Going up right
        #    ... start
        #    ... end
        #    ... board
        #elif ... start end:
        #    # Going up left
        #    ... start
        #    ... end
        #    ... board
        #elif ... start end:
        #    # Going down right
        #    ... start
        #    ... end
        #    ... board
        #else:
        #    # Going down left
        #    ... start
        #    ... end
        #    ... board
        pass


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
    
