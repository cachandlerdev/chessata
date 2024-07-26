from src.experiments.chess_core.pieces.p_base import BasePiece
import pytest


class TestBasePiece:

    def test_is_valid_pos_1(self):
        base = BasePiece()
        assert base._is_valid_pos("a1") is True
        
    
    def test_is_valid_pos_2(self):
        base = BasePiece()
        assert base._is_valid_pos("g4") is True
    
    
    def test_is_valid_pos_3(self):
        base = BasePiece()
        assert base._is_valid_pos("z1") is False
    
    
    def test_is_valid_pos_4(self):
        base = BasePiece()
        assert base._is_valid_pos("f0") is False
    
    
    def test_is_valid_pos_5(self):
        base = BasePiece()
        assert base._is_valid_pos("d9") is False


    def test_get_diagonal_end_1(self):
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
    
    
    def test_get_diagonal_end_2(self):
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
    
    
    def test_get_diagonal_end_3(self):
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
    
    
    def test_get_diagonal_end_4(self):
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
    
    
    def test_get_diagonal_end_error_1(self):
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
    
    
    def test_get_diagonal_end_error_2(self):
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
    
    
    def test_get_diagonal_end_error_3(self):
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
    
