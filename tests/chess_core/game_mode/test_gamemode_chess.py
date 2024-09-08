from src.chess_core.game_mode.gamemode_chess import _identify_move_type
from src.chess_core.structs.move_type import MoveType
from src.chess_core.game_match.match_chess import ChessMatch
from src.chess_core.pieces.p_base import BasePiece
from src.chess_core.pieces.p_bishop import BishopPiece
from src.chess_core.pieces.p_king import KingPiece
from src.chess_core.pieces.p_knight import KnightPiece
from src.chess_core.pieces.p_pawn import PawnPiece
from src.chess_core.pieces.p_queen import QueenPiece
from src.chess_core.pieces.p_rook import RookPiece
from src.chess_core.game_mode.gamemode_chess import *
import pytest

class TestChessGameMode:

    # Get board states
 
    def test_get_pawn_obj(self):
        pawn = get_piece_object(1)
        assert isinstance(pawn, BasePiece)
        assert isinstance(pawn, PawnPiece)

        
    def test_get_rook_obj(self):
        rook = get_piece_object(2)
        assert isinstance(rook, BasePiece)
        assert isinstance(rook, RookPiece)


    def test_get_knight_obj(self):
        knight = get_piece_object(3)
        assert isinstance(knight, BasePiece)
        assert isinstance(knight, KnightPiece)
        

    def test_get_bishop_obj(self):
        
        bishop = get_piece_object(4)
        assert isinstance(bishop, BasePiece)
        assert isinstance(bishop, BishopPiece)


    def test_get_queen_obj(self):
        
        queen = get_piece_object(5)
        assert isinstance(queen, BasePiece)
        assert isinstance(queen, QueenPiece)
        

    def test_get_king_obj(self):
        
        king = get_piece_object(6)
        assert isinstance(king, BasePiece)
        assert isinstance(king, KingPiece)
    
    
    def test_identify_move_type_en_passant_1(self):
        
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
        assert _identify_move_type("e5", "f6", board) == MoveType.EN_PASSANT


    def test_identify_move_type_en_passant_2(self):
        
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
        assert _identify_move_type("d5", "c6", board) == MoveType.EN_PASSANT
    
    
    def test_identify_move_type_en_passant_3(self):
        
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
        assert _identify_move_type("e4", "d3", board) == MoveType.EN_PASSANT
    
    
    def test_identify_move_type_en_passant_4(self):
        
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
        assert _identify_move_type("e4", "f3", board) == MoveType.EN_PASSANT
    
    # TODO: Castling checks
    # Regular checks
    # Promotion checks
    
    def test_identify_move_type_promotion_1(self):
        
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
        assert _identify_move_type("a7", "a8", board) == MoveType.PROMOTION
    
    
    def test_identify_move_type_promotion_2(self):
        
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
        assert _identify_move_type("h2", "h1", board) == MoveType.PROMOTION
    
    
    # TODO: Add a bunch of update game state tests for castling, moving, kings, pawns, etc.
    
    def test_update_game_state_en_passant_1(self):
        
        board = [
             0, -6,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  1,  0,  0,  0,
             0,  6,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        move_piece_at_pos(match, "e2", "e4")
        assert match.is_exposed_to_en_passant("e4") is True
    
    
    def test_update_game_state_en_passant_2(self):
        
        board = [
             0, -6,  0,  0,  0,  0,  0,  0,
             0,  0, -1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  6,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        move_piece_at_pos(match, "c7", "c5")
        assert match.is_exposed_to_en_passant("c5") is True
    
    
    # TODO Check pawn movement after crosses
    # I think I found a bug where either it thought I was in check, but I wasn't
    # or it thought I couldn't move a pawn for some reason
    # not sure how to replicate yet
    # maybe a match update issue?

    # TODO Also add more checkmate tests because I'm pretty sure that game was
    # checkmate for white