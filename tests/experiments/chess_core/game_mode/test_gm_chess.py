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


    # Get piece names
        
    def test_get_white_pawn(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(1) == "White Pawn"
    
    
    def test_get_white_rook(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(2) == "White Rook"
        

    def test_get_white_knight(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(3) == "White Knight"
    
    
    def test_get_white_bishop(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(4) == "White Bishop"


    def test_get_white_queen(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(5) == "White Queen"
    
    
    def test_get_white_king(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(6) == "White King"


    def test_get_black_pawn(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-1) == "Black Pawn"
    
    
    def test_get_black_rook(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-2) == "Black Rook"


    def test_get_black_knight(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-3) == "Black Knight"
    


    def test_get_black_bishop(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-4) == "Black Bishop"


    def test_get_black_queen(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-5) == "Black Queen"
    

    def test_get_black_king(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(-6) == "Black King"
    
    
    def test_get_empty1(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(0) == "Empty"


    def test_get_empty2(self):
        mode = ChessGameMode()
        assert mode.get_piece_type(14) == "Empty"


    # Get pieces

    def test_get_white_pawn_on_initial_board(self):
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
        assert mode.get_piece_at_pos(initial_board, "a2") == 1


    def test_get_black_king_on_initial_board(self):
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
        assert mode.get_piece_at_pos(initial_board, "d8") == -6


    def test_get_white_bishop_on_different_board(self):
        mode = ChessGameMode()
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
        assert mode.get_piece_at_pos(board, "f4") == 4

    
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
