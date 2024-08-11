from src.chess_core.pieces.p_base import BasePiece
#from p_base import BasePiece
import pytest


class TestBasePiece:



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


    
