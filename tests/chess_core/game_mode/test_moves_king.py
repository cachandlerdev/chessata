from src.chess_core.structs.piece_type import PieceType
from src.chess_core.game_match.match_chess import ChessMatch
from src.chess_core.game_mode.gamemode_chess import ChessGameMode
from src.chess_core.structs.game_state import GameState
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
             0,  0,  0, -6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "d4", "d3")
    
    
    def test_move_puts_king_in_check_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "f4", "f5")
    
    
    def test_move_puts_king_in_check_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -2,
             0,  0,  0, -6,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "f4", "f5")
    
    
    def test_move_puts_king_in_check_4(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -6,  0,  6,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  2,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        with pytest.raises(ValueError, match="Illegal move."):
            mode.move_piece_at_pos(match, "d4", "d3")
    
    
    def test_is_in_checkmate_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            -6,  5,  6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, False, PieceType.QUEEN) == GameState.WHITE_WIN
    
    
    def test_is_in_checkmate_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             6, -5, -6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.BLACK_WIN
    
    
    def test_is_in_checkmate_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -6,  0,  0,  0,  0,  0,
             6,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -3,  0,  0,  0,  0,
             0,  0,  0,  0, -5,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        mode.move_piece_at_pos(match, "e1", "a1")
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.BLACK_WIN
    
    
    
    def test_is_in_check_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -1,
             0, -6,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0, -3,  0,  0,  0, -1,  0,
             0,  0,  0,  0, -1,  0,  1,  0,
             0,  0,  0,  0,  1,  3,  0,  0,
            -2,  0,  0,  0,  6,  4,  3,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.WHITE_CHECK
    
    
    def test_is_not_in_checkmate_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0, -6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  6,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.NOT_OVER
    
    
    def test_is_in_stalemate_1(self):
        mode = ChessGameMode()
        initial_board = [
            -6,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  5,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  6,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, False, PieceType.QUEEN) == GameState.STALEMATE
    
    
    def test_is_in_stalemate_2(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0, -6,  0,
            -4,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -1,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0,  0,  0,  0,  0,  0,  6,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.STALEMATE
    
    
    def test_is_in_stalemate_3(self):
        mode = ChessGameMode()
        initial_board = [
             0,  2,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            -1,  0,  0,  2,  0,  0,  0,  0,
            -6,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  6,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, False, PieceType.QUEEN) == GameState.STALEMATE
    
    
    def test_is_in_stalemate_4(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  6,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -5,  0, -6,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, True, PieceType.QUEEN) == GameState.STALEMATE
    
    
    def test_is_not_in_stalemate_1(self):
        mode = ChessGameMode()
        initial_board = [
             0,  0,  0,  0,  0,  0,  6,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -5,  0, -6,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(initial_board)
        assert mode.resolve_game_state(match, False, PieceType.QUEEN) == GameState.NOT_OVER
    
    
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
             0, -4,  0,  0,  0,  0,  0,  0,
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
             0,  0,  0,  0,  0,  0, -2,  0,
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
             0,  0,  0,  0, -4,  0,  0,  0,
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
    
    
