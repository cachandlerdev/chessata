from src.experiments.chess_core.pieces.p_base import BasePiece
from src.experiments.chess_core.pieces.p_bishop import BishopPiece
from src.experiments.chess_core.pieces.p_king import KingPiece
from src.experiments.chess_core.pieces.p_knight import KnightPiece
from src.experiments.chess_core.pieces.p_pawn import PawnPiece
from src.experiments.chess_core.pieces.p_queen import QueenPiece
from src.experiments.chess_core.pieces.p_rook import RookPiece
from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode
import pytest

class TestChessGameMode:

    # Get board states

    def test_get_initial_board(self):
        mode = ChessGameMode()
        expected = [
            -2, -3, -4, -6, -5, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  6,  5,  4,  3,  2,
            ]
        assert mode.get_initial_board() == expected

 
    def test_get_pawn_obj(self):
        mode = ChessGameMode()
        pawn = mode.get_piece_object(1)
        assert isinstance(pawn, BasePiece)
        assert isinstance(pawn, PawnPiece)

        
    def test_get_rook_obj(self):
        mode = ChessGameMode()
        rook = mode.get_piece_object(2)
        assert isinstance(rook, BasePiece)
        assert isinstance(rook, RookPiece)


    def test_get_knight_obj(self):
        mode = ChessGameMode()
        knight = mode.get_piece_object(3)
        assert isinstance(knight, BasePiece)
        assert isinstance(knight, KnightPiece)
        

    def test_get_bishop_obj(self):
        mode = ChessGameMode()
        bishop = mode.get_piece_object(4)
        assert isinstance(bishop, BasePiece)
        assert isinstance(bishop, BishopPiece)


    def test_get_queen_obj(self):
        mode = ChessGameMode()
        queen = mode.get_piece_object(5)
        assert isinstance(queen, BasePiece)
        assert isinstance(queen, QueenPiece)
        

    def test_get_king_obj(self):
        mode = ChessGameMode()
        king = mode.get_piece_object(6)
        assert isinstance(king, BasePiece)
        assert isinstance(king, KingPiece)
