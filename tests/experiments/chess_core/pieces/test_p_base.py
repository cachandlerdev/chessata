from src.experiments.chess_core.pieces.p_base import BasePiece
import pytest


class TestBasePiece:
    
    def test_collision_with_no_pieces_throws_exception(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="No piece at start position."):
            base.does_move_collide("d5", "d6", board)
            
            
    def test_collision_with_no_movement_throws_exception(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="Start and end positions match."):
            base.does_move_collide("d5", "d5", board)
            
    
    def test_no_collision(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d5", "d6", board) == 0
    

    def test_friendly_collision_up_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f4", "f5", board) == 2
        
    
    def test_friendly_collision_up_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f4", "f6", board) == 2
        
        
    def test_friendly_collision_down_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  5,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  4,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d5", "d3", board) == 2
        
        
    def test_black_friendly_collision_down_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d6", "d5", board) == 2
    

    def test_friendly_collision_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  3,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d4", "b4", board) == 2
    

    def test_friendly_collision_right_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  2,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("c4", "f4", board) == 2
        

    def test_friendly_collision_on_way_right_four_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  2,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("c4", "g4", board) == 2
        
    
    def test_friendly_collision_on_way_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f2", "d2", board) == 2


    def test_friendly_collision_on_way_up_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("e4", "e7", board) == 2


    def test_friendly_collision_on_way_down_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  5,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("e7", "e5", board) == 2
        
        
    def test_friendly_collision_up_right_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d3", "g4", board) == 2
        

    def test_friendly_collision_up_left_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f3", "c6", board) == 2
        
        
    def test_friendly_collision_down_right_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d5", "e4", board) == 2

        
    def test_friendly_collision_down_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f5", "d3", board) == 2
        
        
        # Enemy collision
        
        
    def test_enemy_collision_up_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f4", "f5", board) == 1
        
    
    def test_enemy_collision_up_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f4", "f6", board) == 1
        
        
    def test_enemy_collision_down_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -5,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  4,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d5", "d3", board) == 1
        
        
    def test_white_enemy_collision_down_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d6", "d5", board) == 1
    

    def test_enemy_collision_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -3,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d4", "b4", board) == 1
    

    def test_enemy_collision_right_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -2,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("c4", "f4", board) == 1
        

    def test_enemy_collision_on_way_right_four_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  2,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("c4", "g4", board) == 1
        
    
    def test_enemy_collision_on_way_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f2", "d2", board) == 1


    def test_enemy_collision_on_way_up_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("e4", "e7", board) == 1


    def test_enemy_collision_on_way_down_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  5,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("e7", "e5", board) == 1
        
        
    def test_enemy_collision_up_right_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d3", "f5", board) == 1
        

    def test_enemy_collision_up_left_three_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f3", "c6", board) == 1
        
        
    def test_enemy_collision_down_right_one_space(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -3,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("d5", "e4", board) == 1

        
    def test_enemy_collision_down_left_two_spaces(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base.does_move_collide("f5", "d3", board) == 1
        
        # Movement type
        
    def test_get_empty__movement_type(self):
        base = BasePiece()
        with pytest.raises(ValueError, match="No movement type specified."):
            base._get__movement_type_used("a1", "b3", "")
    

    def test_get_only_one__movement_type1(self):
        base = BasePiece()
        assert base._get__movement_type_used("a1", "a2", "|") == "|"
    
    
    def test_get_only_one__movement_type2(self):
        base = BasePiece()
        assert base._get__movement_type_used("c4", "d4", "+") == "+"
    
    
    def test_get_only_one__movement_type3(self):
        base = BasePiece()
        assert base._get__movement_type_used("e3", "f4", "X") == "X"
    
    
    def test_get_only_one__movement_type4(self):
        base = BasePiece()
        assert base._get__movement_type_used("e3", "f4", "V") == "V"
        
    
    def test_get_L__movement_type(self):
        base = BasePiece()
        assert base._get__movement_type_used("b1", "c3", "L") == "L"
    
    # King movement
    
    def test_get_king_horizontal__movement_type_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("e4", "d4", "+X") == "+"
    
    
    def test_get_king_horizontal__movement_type_up(self):
        base = BasePiece()
        assert base._get__movement_type_used("c4", "c5", "+X") == "+"
        
    
    def test_get_king_horizontal__movement_type_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("g2", "h2", "+X") == "+"
    
    
    def test_get_king_horizontal__movement_type_down(self):
        base = BasePiece()
        assert base._get__movement_type_used("b6", "b5", "+X") == "+"
    
    
    def test_get_king_diagonal__movement_type_up_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("e4", "d5", "+X") == "X"
    
    
    def test_get_king_diagonal__movement_type_up_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("a1", "b2", "+X") == "X"
        
    
    def test_get_king_diagonal__movement_type_down_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("g3", "f2", "+X") == "X"
    
    
    def test_get_king_diagonal__movement_type_down_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("f5", "g4", "+X") == "X"
    
    # Queen movement
    
    def test_get_queen_horizontal__movement_type_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("h4", "b4", "+X") == "+"
    
    
    def test_get_queen_horizontal__movement_type_up(self):
        base = BasePiece()
        assert base._get__movement_type_used("c4", "c8", "+X") == "+"
        
    
    def test_get_queen_horizontal__movement_type_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("a2", "h2", "+X") == "+"
    
    
    def test_get_queen_horizontal__movement_type_down(self):
        base = BasePiece()
        assert base._get__movement_type_used("b6", "b4", "+X") == "+"
    
    
    def test_get_queen_diagonal__movement_type_up_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("e4", "c6", "+X") == "X"
    
    
    def test_get_queen_diagonal__movement_type_up_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("a1", "d4", "+X") == "X"
        
    
    def test_get_queen_diagonal__movement_type_down_left(self):
        base = BasePiece()
        assert base._get__movement_type_used("g3", "e1", "+X") == "X"
    
    
    def test_get_queen_diagonal__movement_type_down_right(self):
        base = BasePiece()
        assert base._get__movement_type_used("b4", "e1", "+X") == "X"


    def test__is_valid_pos_1(self):
        base = BasePiece()
        assert base._is_valid_pos("a1") is True
        
    
    def test__is_valid_pos_2(self):
        base = BasePiece()
        assert base._is_valid_pos("g4") is True
    
    
    def test__is_valid_pos_3(self):
        base = BasePiece()
        assert base._is_valid_pos("z1") is False
    
    
    def test__is_valid_pos_4(self):
        base = BasePiece()
        assert base._is_valid_pos("f0") is False
    
    
    def test__is_valid_pos_5(self):
        base = BasePiece()
        assert base._is_valid_pos("d9") is False
        
        
    # Valid moves
        
    def test_get_vertical_valid_moves_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d6", "d7", "d8", "d4", "d3", "d2", "d1"]
        assert base._get_valid_vertical_moves("d5", board, "+", False) == expected


    def test_get_vertical_valid_moves_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -5,  0,
            ]
        expected = ["g2", "g3", "g4", "g5", "g6", "g7", "g8"]
        assert base._get_valid_vertical_moves("g1", board, "+", False) == expected
    
    
    def test_get_vertical_valid_moves_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  5,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["f7", "f6", "f5", "f4", "f3", "f2", "f1"]
        assert base._get_valid_vertical_moves("f8", board, "+", False) == expected
    
    
    def test_get_vertical_valid_moves_collision_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  3,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  2,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b3", "b4", "b1"]
        assert base._get_valid_vertical_moves("b2", board, "+", False) == expected


    def test_get_vertical_valid_moves_collision_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d7", "d8"]
        assert base._get_valid_vertical_moves("d6", board, "+", False) == expected


    def test_get_vertical_valid_moves_collision_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["f6", "f4"]
        assert base._get_valid_vertical_moves("f5", board, "+", False) == expected


    def test_get_vertical_valid_moves_collision_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             5,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = []
        assert base._get_valid_vertical_moves("a5", board, "+", False) == expected


    def test_get_vertical_cross_valid_moves(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  1,  5,  1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["f7", "f6", "f5", "f4", "f3", "f2", "f1"]
        assert base._get_valid_cross_moves("f8", board) == expected


    def test__get_valid_cross_moves_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d6", "d7", "d8", "d4", "d3", "d2", "d1", "c5", "b5", "a5", "e5", "f5", "g5", "h5"]
        assert base._get_valid_cross_moves("d5", board) == expected


    def test__get_valid_cross_moves_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -1,  0,
             0,  0,  0,  0,  0,  0, -5,  0,
            ]
        expected = ["f1", "e1", "d1", "c1", "b1", "a1", "h1"]
        assert base._get_valid_cross_moves("g1", board) == expected
    
    
    def test__get_valid_cross_moves_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             5,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b5", "c5", "d5", "e5", "f5", "g5", "h5"]
        assert base._get_valid_cross_moves("a5", board) == expected
    
    
    def test__get_valid_cross_moves_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0,  0,  0,  0,  0,  0,  5,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["g5", "f5", "e5", "d5", "c5", "b5", "a5"]
        assert base._get_valid_cross_moves("h5", board) == expected
    
    
    def test__get_valid_cross_moves_collision_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  3,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  2,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b3", "b4", "b1", "c2", "d2", "e2", "f2", "g2", "h2"]
        assert base._get_valid_cross_moves("b2", board) == expected


    def test__get_valid_cross_moves_collision_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  1,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d7", "d8", "c6", "b6", "a6", "e6"]
        assert base._get_valid_cross_moves("d6", board) == expected


    def test__get_valid_cross_moves_collision_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -4,  0, -2,  0, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["f6", "f4", "e5", "g5"]
        assert base._get_valid_cross_moves("f5", board) == expected


    def test__get_valid_cross_moves_collision_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             5,  2,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = []
        assert base._get_valid_cross_moves("a5", board) == expected
        
    
    def test__get_valid_diagonal_moves_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["c6", "b7", "a8", "e6", "f7", "g8", "c4", "b3", "a2", "e4", "f3", "g2", "h1"]
        assert base._get_valid_diagonal_moves("d5", board) == expected


    def test__get_valid_diagonal_moves_2(self):
        base = BasePiece()
        board = [
             3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b7", "c6", "d5", "e4", "f3", "g2", "h1"]
        assert base._get_valid_diagonal_moves("a8", board) == expected
        
        
    def test__get_valid_diagonal_moves_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  3,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["g7", "f6", "e5", "d4", "c3", "b2", "a1"]
        assert base._get_valid_diagonal_moves("h8", board) == expected
    
    
    def test__get_valid_diagonal_moves_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b2", "c3", "d4", "e5", "f6", "g7", "h8"]
        assert base._get_valid_diagonal_moves("a1", board) == expected


    def test__get_valid_diagonal_moves_5(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  3,
            ]
        expected = ["g2", "f3", "e4", "d5", "c6", "b7", "a8"]
        assert base._get_valid_diagonal_moves("h1", board) == expected


    def test__get_valid_diagonal_moves_collision_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  3,
            ]
        expected = ["g2"]
        assert base._get_valid_diagonal_moves("h1", board) == expected


    def test__get_valid_diagonal_moves_collision_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  4,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b2", "c3"]
        assert base._get_valid_diagonal_moves("a1", board) == expected


    def test__get_valid_diagonal_moves_collision_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  3,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["g7", "f6", "e5"]
        assert base._get_valid_diagonal_moves("h8", board) == expected


    def test__get_valid_diagonal_moves_collision_4(self):
        base = BasePiece()
        board = [
             3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b7", "c6", "d5", "e4", "f3"]
        assert base._get_valid_diagonal_moves("a8", board) == expected


    def test__get_valid_diagonal_moves_collision_5(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  2,
            ]
        expected = ["c6", "e6", "c4", "b3", "e4", "f3", "g2"]
        assert base._get_valid_diagonal_moves("d5", board) == expected


    def test__get_valid_diagonal_moves_collision_6(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = []
        assert base._get_valid_diagonal_moves("d5", board) == expected


    def test__get_diagonal_end_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base._get_diagonal_end("a1", 1, 1, board) == "h8"
    
    
    def test__get_diagonal_end_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base._get_diagonal_end("a8", 1, -1, board) == "h1"
    
    
    def test__get_diagonal_end_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base._get_diagonal_end("e1", -1, 1, board) == "a5"
    
    
    def test__get_diagonal_end_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert base._get_diagonal_end("h5", -1, -1, board) == "d1"
    
    
    def test__get_diagonal_end_error_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="Invalid direction."):
            base._get_diagonal_end("a1", 1, 0, board)
    
    
    def test__get_diagonal_end_error_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="Invalid starting position."):
            base._get_diagonal_end("a0", 1, 1, board)
    
    
    def test__get_diagonal_end_error_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="Invalid starting position."):
            base._get_diagonal_end("m3", 1, 1, board)


    def test__get_valid_v_moves_none_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = []
        assert base._get_valid_v_moves("d5", board) == expected
        

    def test__get_valid_v_moves_none_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = []
        assert base._get_valid_v_moves("c3", board) == expected


    def test__get_valid_v_moves_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -3,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d4"]
        assert base._get_valid_v_moves("c3", board) == expected
        
        
    def test__get_valid_v_moves_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  0,  2,  4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["f5"]
        assert base._get_valid_v_moves("e6", board) == expected


    def test__get_valid_v_moves_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  2,  2,  4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["d5", "f5"]
        assert base._get_valid_v_moves("e6", board) == expected
    
    
    def test__get_valid_v_moves_4(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -4,  2, -3,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["c4", "e4"]
        assert base._get_valid_v_moves("d3", board) == expected


    def test__get_valid_L_moves_1(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  3,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["c5", "d6", "f6", "g5", "g3", "f2", "d2", "c3"]
        assert base._get_valid_L_moves("e4", board) == expected
        
        
    def test__get_valid_L_moves_2(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["h7", "g6", "e6", "d7"]
        assert base._get_valid_L_moves("f8", board) == expected
    
    
    def test__get_valid_L_moves_3(self):
        base = BasePiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            -3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        expected = ["b7", "c6", "c4", "b3"]
        assert base._get_valid_L_moves("a5", board) == expected
    
    
    def test__get_valid_L_moves_4(self):
        base = BasePiece()
        board = [
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  3,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
            ]
        expected = []
        assert base._get_valid_L_moves("e4", board) == expected


    # TODO: Add attack tests
    
    def test__relative_to_absolute_pos_1(self):
        base = BasePiece()
        assert base._relative_to_absolute_pos("a3", (2, 1)) == "c4"
        
    
    def test__relative_to_absolute_pos_2(self):
        base = BasePiece()
        assert base._relative_to_absolute_pos("d7", (-2, -1)) == "b6"
    
    
    def test__relative_to_absolute_pos_3(self):
        base = BasePiece()
        assert base._relative_to_absolute_pos("f5", (2, -1)) == "h4"
    
    
    def test__relative_to_absolute_pos_4(self):
        base = BasePiece()
        assert base._relative_to_absolute_pos("e1", (-2, 1)) == "c2"
    
    
    def test__relative_to_absolute_pos_5(self):
        base = BasePiece()
        with pytest.raises(ValueError, match="Invalid starting position."):
            base._relative_to_absolute_pos("z9", (2, 1))
    
    
    def test__relative_to_absolute_pos_6(self):
        base = BasePiece()
        with pytest.raises(ValueError, match="Invalid transformation."):
            base._relative_to_absolute_pos("a3", (-5, 1))
    

    def test__relative_to_absolute_pos_7(self):
        base = BasePiece()
        with pytest.raises(ValueError, match="Invalid transformation."):
            base._relative_to_absolute_pos("a1", (2, -1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















































































