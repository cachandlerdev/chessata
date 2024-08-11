from src.chess_core.structs.move_type import MoveType
from src.chess_core.game_mode.match_chess import ChessMatch
from src.chess_core.pieces.p_base import BasePiece
from src.chess_core.pieces.p_bishop import BishopPiece
from src.chess_core.pieces.p_king import KingPiece
from src.chess_core.pieces.p_knight import KnightPiece
from src.chess_core.pieces.p_pawn import PawnPiece
from src.chess_core.pieces.p_queen import QueenPiece
from src.chess_core.pieces.p_rook import RookPiece
from src.chess_core.game_mode.gm_chess import ChessGameMode
import pytest

class TestChessGameMode:

    # Get board states
 
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
    
    
    def test_identify_move_type_en_passant_1(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("e5", "f6", board) == MoveType.EN_PASSANT


    def test_identify_move_type_en_passant_2(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -1,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("d5", "c6", board) == MoveType.EN_PASSANT
    
    
    def test_identify_move_type_en_passant_3(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1, -1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("e4", "d3", board) == MoveType.EN_PASSANT
    
    
    def test_identify_move_type_en_passant_4(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("e4", "f3", board) == MoveType.EN_PASSANT
    
    # TODO: Castling checks
    # Regular checks
    # Promotion checks
    
    def test_identify_move_type_promotion_1(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("a7", "a8", board) == MoveType.PROMOTION
    
    
    def test_identify_move_type_promotion_2(self):
        mode = ChessGameMode()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        assert mode._identify_move_type("h2", "h1", board) == MoveType.PROMOTION
