from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode
import pytest

class TestChessMoves:
    """A separate class for testing board moves because this file might get big :)"""

    def test_move_empty_square_exception(self):
        mode = ChessGameMode()
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
        empty_square = "d4"
        end = "d5"
        with pytest.raises(ValueError, match="Invalid piece number."):
            mode.move_piece_at_pos(initial_board, empty_square, end)
        

    def test_move_piece_nowhere(self):
        mode = ChessGameMode()
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
        with pytest.raises(ValueError, match="Start and end positions match."):
            mode.move_piece_at_pos(initial_board, "b7", "b7")

    
    def test_move_white_pawn_one_space(self):
        mode = ChessGameMode()
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
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "a2", "a3") == final_board
        

    def test_move_white_pawn_two_spaces(self):
        mode = ChessGameMode()
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
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  1,  1,  1,  0,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f2", "f4") == final_board


    def test_move_black_pawn_one_space(self):
        mode = ChessGameMode()
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
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1,  0, -1, -1,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f7", "f6") == final_board


    def test_move_black_pawn_two_spaces(self):
        mode = ChessGameMode()
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
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1,  0, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d7", "d5") == final_board
    

    def test_move_white_rook_up_one_space(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d4", "d5") == final_board


    def test_move_white_rook_up_three_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  2, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d4", "d7") == final_board
        
        
    def test_move_white_rook_down_one_space(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f6", "f5") == final_board
        

    def test_move_white_rook_down_four_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  2,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "e6", "e2") == final_board


    def test_move_white_rook_left_two_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f4", "d4") == final_board


    def test_move_white_rook_right_three_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "e6", "h6") == final_board


    def test_move_black_rook_up_one_space(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3,  0,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3,  0,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d4", "d5") == final_board


    def test_move_black_rook_up_three_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0, -2, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d4", "d7") == final_board
        
        
    def test_move_black_rook_down_one_space(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f6", "f5") == final_board
        

    def test_move_black_rook_down_four_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0, -2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1, -2,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "e6", "e2") == final_board


    def test_move_black_rook_left_two_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "f4", "d4") == final_board


    def test_move_black_rook_right_three_spaces(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0, -2,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "e6", "h6") == final_board
        
    
    def test_move_white_knight_tall_L_right(self):
        mode = ChessGameMode()
        initial_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1,  0,  0, -1,  0, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  3,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  0,  0,  0,  1,
             0,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.move_piece_at_pos(initial_board, "d3", "e5") == final_board
        
        # need to test jumping

        # Coming back to these later once stuff is actually implemented

        
        # Need to add attack tests too
        
        
        
        
        
        
        
        
        
        
        
        
        
