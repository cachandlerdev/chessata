from src.chess_core.board_utils import *
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


    def test_relative_to_absolute_pos_1(self):
        assert relative_to_absolute_pos("a3", (2, 1)) == "c4"
        
    
    def test_relative_to_absolute_pos_2(self):
        assert relative_to_absolute_pos("d7", (-2, -1)) == "b6"
    
    
    def test_relative_to_absolute_pos_3(self):
        assert relative_to_absolute_pos("f5", (2, -1)) == "h4"
    
    
    def test_relative_to_absolute_pos_4(self):
        assert relative_to_absolute_pos("e1", (-2, 1)) == "c2"
    
    
    def test_relative_to_absolute_pos_5(self):
        with pytest.raises(ValueError, match="Invalid starting position."):
            relative_to_absolute_pos("z9", (2, 1))
    
    
    def test_relative_to_absolute_pos_6(self):
        with pytest.raises(ValueError, match="Invalid transformation."):
            relative_to_absolute_pos("a3", (-5, 1))
    

    def test_relative_to_absolute_pos_7(self):
        with pytest.raises(ValueError, match="Invalid transformation."):
            relative_to_absolute_pos("a1", (2, -1))
    
    
    def test_absolute_to_relative_pos_1(self):
        assert absolute_to_relative_pos("a3", "c4") == (2, 1)
    
    
    def test_absolute_to_relative_pos_2(self):
        assert absolute_to_relative_pos("d7", "b6") == (-2, -1)
    
    
    def test_absolute_to_relative_pos_3(self):
        assert absolute_to_relative_pos("f5", "h4") == (2, -1)
    
    
    def test_absolute_to_relative_pos_4(self):
        assert absolute_to_relative_pos("e1", "c2") == (-2, 1)
    
    
    def test_absolute_to_relative_pos_5(self):
        with pytest.raises(ValueError, match="Invalid starting position."):
            absolute_to_relative_pos("z9", "c2")
    
    
    def test_absolute_to_relative_pos_6(self):
        with pytest.raises(ValueError, match="Invalid final point."):
            absolute_to_relative_pos("b3", "t2")
    
    
    def test_is_valid_pos_1(self):
        assert is_valid_pos("a1") is True
        
    
    def test_is_valid_pos_2(self):
        assert is_valid_pos("g4") is True
    
    
    def test_is_valid_pos_3(self):
        assert is_valid_pos("z1") is False
    
    
    def test_is_valid_pos_4(self):
        assert is_valid_pos("f0") is False
    
    
    def test_is_valid_pos_5(self):
        assert is_valid_pos("d9") is False
    
    
    def test_is_valid_pos_6(self):
        assert is_valid_pos("b") is False
    
    
    def test_is_valid_pos_7(self):
        assert is_valid_pos("bw14") is False


    def test_find_piece_pos_1(self):
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -4,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  2,
            ]
        assert find_piece_pos(-4, board) == "b4"
    
    
    def test_find_piece_pos_2(self):
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert find_piece_pos(6, board) == "d3"
    
    
    def test_find_piece_pos_3(self):
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        with pytest.raises(ValueError, match="Piece not found."):
            find_piece_pos(-6, board)


    def test_get_pos_from_index_1(self):
        assert get_pos_from_index(33) == "b4"
    
    
    def test_get_pos_from_index_2(self):
        assert get_pos_from_index(43) == "d3"
    
    
    def test_get_pos_from_index_3(self):
        assert get_pos_from_index(0) == "a8"
    
    
    def test_get_pos_from_index_4(self):
        assert get_pos_from_index(56) == "a1"
    
    
    def test_get_pos_from_index_5(self):
        assert get_pos_from_index(9) == "b7"