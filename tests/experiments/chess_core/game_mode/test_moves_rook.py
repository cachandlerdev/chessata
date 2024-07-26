from src.experiments.chess_core.game_mode.match_chess import ChessMatch
from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode
import pytest


class TestRookMoves:
    
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

        # TODO: Attack tests
        # Illegal checks