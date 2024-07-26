from src.experiments.chess_core.game_mode.match_chess import ChessMatch
from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode
import pytest


class TestKnightMoves:

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