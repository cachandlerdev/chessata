from src.experiments.chess_core.game_mode.match_chess import ChessMatch
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
        match = ChessMatch(initial_board)
        empty_square = "d4"
        end = "d5"
        with pytest.raises(ValueError, match="Invalid piece number."):
            mode.move_piece_at_pos(match, empty_square, end)
        

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
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Start and end positions match."):
            mode.move_piece_at_pos(match, "b7", "b7")
    
    
    def test_illegal_move_1(self):
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
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "a1", "a5")


    
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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "a2", "a3")
        assert match.board == final_board
        

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
        match = ChessMatch(initial_board)
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  0,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        mode.move_piece_at_pos(match, "f2", "f4")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1,  0, -1, -1,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        mode.move_piece_at_pos(match, "f7", "f6")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
        final_board = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1,  0, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        mode.move_piece_at_pos(match, "d7", "d5")
        assert match.board == final_board
    

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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "d4", "d5")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "d4", "d7")
        assert match.board == final_board
        
        
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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "f6", "f5")
        assert match.board == final_board
        

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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "e6", "e2")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "f4", "d4")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "e6", "h6")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "d4", "d5")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "d4", "d7")
        assert match.board == final_board
        
        
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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "f6", "f5")
        assert match.board == final_board
        

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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "e6", "e2")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "f4", "d4")
        assert match.board == final_board


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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "e6", "h6")
        assert match.board == final_board
        
    
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
        match = ChessMatch(initial_board)
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
        mode.move_piece_at_pos(match, "d3", "e5")
        assert match.board == final_board
        
        
        # Need to add attack tests too
        
        
        
        
        
        
        
        
        
        
        
        
        
