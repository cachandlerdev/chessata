from src.experiments.chess_core.game_mode.match_chess import ChessMatch
from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode
import pytest


class TestKingMoves:

    def test_illegal_move_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "d3", "d5")
    

    def test_illegal_move_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "d3", "e5")
    
    
    def test_move_puts_king_in_check_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "d3", "e5")
        # TODO
        assert False
    
    
    def test_is_king_in_check_1(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("d1", True, match) is True

    
    
    def test_is_king_in_check_2(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  6,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", True, match) is True
    
    
    def test_is_king_in_check_3(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  6,  0,  0, -5,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", True, match) is True
    
    
    def test_is_king_in_check_4(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  4,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", False, match) is True
    
    
    def test_is_king_in_check_5(self):
        mode = ChessGameMode()
        board = [
            -4,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  6,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("h1", True, match) is True
    
    
    def test_is_king_in_check_6(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -3,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", True, match) is True
    
    
    def test_is_king_in_check_7(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  3,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", False, match) is True
    
    
    def test_is_king_in_check_8(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("c2", True, match) is True
    
    
    def test_is_king_in_check_9(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  0,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f3", True, match) is True
    
    
    def test_is_king_in_check_10(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -6,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", False, match) is True
    
    
    def test_king_is_not_in_check_1(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  6,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", True, match) is False
    
    
    def test_king_is_not_in_check_2(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", True, match) is False
    
    
    def test_king_is_not_in_check_3(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -4,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", True, match) is False
    
    
    def test_king_is_not_in_check_4(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -2,  0,  0,  0,
             0,  0,  0,  0,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", True, match) is False
    
    
    def test_king_is_not_in_check_5(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0, -4,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("e4", True, match) is False
    
    
    def test_king_is_not_in_check_6(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -3,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("f5", False, match) is False
    
    
    def test_king_is_not_in_check_7(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("e4", True, match) is False
    
    
    def test_king_is_not_in_check_8(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        assert mode.is_in_check("e4", True, match) is False
    

    def test_kingside_castling_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        final_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  0,  2,  6,  0,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "e1", "g1")
        assert match.board == final_board
    
    
    def test_kingside_castling_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        final_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  6,  2,  0,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "e1", "c1")
        assert match.board == final_board


    def test_kingside_castling_3(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        final_board = [
            -2,  0,  0,  0,  0, -2, -6,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "e8", "g8")
        assert match.board == final_board
    
    
    def test_kingside_castling_4(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        final_board = [
             0,  0, -6, -2,  0,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "e8", "c8")
        assert match.board == final_board
    
    
    def test_kingside_no_castling_out_of_check_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -4,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_out_of_check_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -4,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "c1")
    
    
    def test_kingside_no_castling_out_of_check_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0, -6,  0,  0,  2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  4,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "g8")
    
    
    def test_kingside_no_castling_out_of_check_4(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  4,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "c8")
    
    
    def test_kingside_no_castling_through_check_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -4,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_through_check_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -2,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_through_check_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -2,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_through_check_4(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            -4,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "c1")
    
    
    def test_kingside_no_castling_through_check_5(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -3,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "c1")
    
    
    def test_kingside_no_castling_through_check_6(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  2,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "g8")
    
    
    def test_kingside_no_castling_through_check_7(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  3,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "g8")
    
    
    def test_kingside_no_castling_through_check_8(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "c8")
    
    
    def test_kingside_no_castling_through_check_9(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  5,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "c8")
    
    
    def test_kingside_no_castling_through_check_10(self):
        mode = ChessGameMode()
        initial_board = [
            -2,  0,  0,  0, -6,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  2,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e8", "c8")
    
    
    def test_kingside_no_castling_into_check_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_into_check_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_into_check_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -3,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "g1")
    
    
    def test_kingside_no_castling_into_check_4(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -5,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "c1")
    
    
    def test_kingside_no_castling_into_check_5(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -4,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  6,  0,  0,  2,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "e1", "c1")
    
    
