from src.experiments.chess_core.board_utils import *
import pytest


class TestBoardUtils:

    # Get piece names
        
    def test_get_white_pawn(self):
        assert get_piece_type(1) == "White Pawn"
    
    
    def test_get_white_rook(self):
        assert get_piece_type(2) == "White Rook"
        

    def test_get_white_knight(self):
        assert get_piece_type(3) == "White Knight"
    
    
    def test_get_white_bishop(self):
        assert get_piece_type(4) == "White Bishop"


    def test_get_white_queen(self):
        assert get_piece_type(5) == "White Queen"
    
    
    def test_get_white_king(self):
        assert get_piece_type(6) == "White King"


    def test_get_black_pawn(self):
        assert get_piece_type(-1) == "Black Pawn"
    
    
    def test_get_black_rook(self):
        assert get_piece_type(-2) == "Black Rook"


    def test_get_black_knight(self):
        assert get_piece_type(-3) == "Black Knight"
    

    def test_get_black_bishop(self):
        assert get_piece_type(-4) == "Black Bishop"


    def test_get_black_queen(self):
        assert get_piece_type(-5) == "Black Queen"
    

    def test_get_black_king(self):
        assert get_piece_type(-6) == "Black King"
    
    
    def test_get_empty1(self):
        assert get_piece_type(0) == "Empty"


    def test_get_empty2(self):
        assert get_piece_type(14) == "Empty"

    # Get pieces

    def test_get_white_pawn_on_initial_board(self):
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert get_piece_at_pos(initial_board, "a2") == 1


    def test_get_black_king_on_initial_board(self):
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert get_piece_at_pos(initial_board, "d8") == -6


    def test_get_white_bishop_on_different_board(self):
        board = [
            -2, -3, -4,  0, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  0,  3,  2,
            ]
        assert get_piece_at_pos(board, "f4") == 4


    def test_is_piece_friendly1(self):
        assert is_piece_friendly(1, 1) is True
    
    
    def test_is_piece_friendly2(self):
        assert is_piece_friendly(2, 5) is True
    
    
    def test_is_piece_friendly3(self):
        assert is_piece_friendly(3, -4) is False
    
    
    def test_is_piece_friendly4(self):
        assert is_piece_friendly(-2, 6) is False
    
    
    def test_is_piece_friendly5(self):
        with pytest.raises(ValueError, match="Invalid piece number."):
            is_piece_friendly(0, 5)
    
    
    def test_is_piece_friendly6(self):
        with pytest.raises(ValueError, match="Invalid piece number."):
            is_piece_friendly(-3, 0)
    
    
    def test_is_piece_friendly7(self):
        with pytest.raises(ValueError, match="Invalid piece number."):
            is_piece_friendly(8, 2)
    
    
    def test_is_piece_friendly8(self):
        with pytest.raises(ValueError, match="Invalid piece number."):
            is_piece_friendly(-7, 4)