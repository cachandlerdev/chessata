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
        
    def test_get_empty_movement_type(self):
        base = BasePiece()
        with pytest.raises(ValueError, match="No movement type specified."):
            base.get_movement_type_used("a1", "b3", "")
    

    def test_get_only_one_movement_type1(self):
        base = BasePiece()
        assert base.get_movement_type_used("a1", "a2", "|") == "|"
    
    
    def test_get_only_one_movement_type2(self):
        base = BasePiece()
        assert base.get_movement_type_used("c4", "d4", "+") == "+"
    
    
    def test_get_only_one_movement_type3(self):
        base = BasePiece()
        assert base.get_movement_type_used("e3", "f4", "X") == "X"
    
    
    def test_get_only_one_movement_type4(self):
        base = BasePiece()
        assert base.get_movement_type_used("e3", "f4", "V") == "V"
        
    
    def test_get_L_movement_type(self):
        base = BasePiece()
        assert base.get_movement_type_used("b1", "c3", "L") == "L"
    
    # King movement
    
    def test_get_king_horizontal_movement_type_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("e4", "d4", "+X") == "+"
    
    
    def test_get_king_horizontal_movement_type_up(self):
        base = BasePiece()
        assert base.get_movement_type_used("c4", "c5", "+X") == "+"
        
    
    def test_get_king_horizontal_movement_type_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("g2", "h2", "+X") == "+"
    
    
    def test_get_king_horizontal_movement_type_down(self):
        base = BasePiece()
        assert base.get_movement_type_used("b6", "b5", "+X") == "+"
    
    
    def test_get_king_diagonal_movement_type_up_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("e4", "d5", "+X") == "X"
    
    
    def test_get_king_diagonal_movement_type_up_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("a1", "b2", "+X") == "X"
        
    
    def test_get_king_diagonal_movement_type_down_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("g3", "f2", "+X") == "X"
    
    
    def test_get_king_diagonal_movement_type_down_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("f5", "g4", "+X") == "X"
    
    # Queen movement
    
    def test_get_queen_horizontal_movement_type_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("h4", "b4", "+X") == "+"
    
    
    def test_get_queen_horizontal_movement_type_up(self):
        base = BasePiece()
        assert base.get_movement_type_used("c4", "c8", "+X") == "+"
        
    
    def test_get_queen_horizontal_movement_type_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("a2", "h2", "+X") == "+"
    
    
    def test_get_queen_horizontal_movement_type_down(self):
        base = BasePiece()
        assert base.get_movement_type_used("b6", "b4", "+X") == "+"
    
    
    def test_get_queen_diagonal_movement_type_up_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("e4", "c6", "+X") == "X"
    
    
    def test_get_queen_diagonal_movement_type_up_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("a1", "d4", "+X") == "X"
        
    
    def test_get_queen_diagonal_movement_type_down_left(self):
        base = BasePiece()
        assert base.get_movement_type_used("g3", "e1", "+X") == "X"
    
    
    def test_get_queen_diagonal_movement_type_down_right(self):
        base = BasePiece()
        assert base.get_movement_type_used("b4", "e1", "+X") == "X"
