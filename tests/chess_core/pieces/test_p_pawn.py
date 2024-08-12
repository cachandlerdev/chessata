from src.chess_core.game_match.match_chess import ChessMatch
from src.chess_core.pieces.p_pawn import PawnPiece


class TestPawnPiece:
    def test_pawn_move_1(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d3", "d4"]
        assert pawn.get_valid_moves("d2", match) == expected
        
    
    def test_pawn_move_2(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b5"]
        assert pawn.get_valid_moves("b4", match) == expected
    
    
    def test_pawn_move_3(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c8"]
        assert pawn.get_valid_moves("c7", match) == expected
    
    
    def test_pawn_move_4(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c6", "c5"]
        assert pawn.get_valid_moves("c7", match) == expected
    
    
    def test_pawn_move_5(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f5"]
        assert pawn.get_valid_moves("f6", match) == expected
    
     
    def test_pawn_move_6(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d1"]
        assert pawn.get_valid_moves("d2", match) == expected
    
    
    def test_pawn_move_7(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -2,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn.get_valid_moves("d2", match) == expected
    
    
    def test_pawn_move_8(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn.get_valid_moves("f3", match) == expected
    
    
    def test_pawn_move_9(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -1,  0,  0,  0,  0,  0,
             0,  0,  2,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn.get_valid_moves("c7", match) == expected
    
    
    def test_pawn_move_10(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -1,  0,  0,  0,  0,  0,  0,
             0,  4,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn.get_valid_moves("b5", match) == expected

    
    def test_pawn_cannot_attack_too_far_away(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -2,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d3", "d4"]
        assert pawn.get_valid_moves("d2", match) == expected
    
    
    def test_pawn_attack_1(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -2,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d5", "c5"]
        assert pawn.get_valid_moves("d4", match) == expected


    def test_pawn_attack_2(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -2,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d5", "e5"]
        assert pawn.get_valid_moves("d4", match) == expected


    def test_pawn_attack_3(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -3,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f3", "f4", "g3"]
        assert pawn.get_valid_moves("f2", match) == expected


    def test_pawn_attack_4(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -2,  0, -3,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f3", "f4", "e3", "g3"]
        assert pawn.get_valid_moves("f2", match) == expected


    def test_pawn_en_passant_1(self):
        pawn = PawnPiece()
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
        en_passant = [False, False, False, False, False, True,  False, False,
                      False, False, False, False, False, False, False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        expected = ["e6", "f6"]
        assert pawn.get_valid_moves("e5", match) == expected


    def test_pawn_en_passant_2(self):
        pawn = PawnPiece()
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
        en_passant = [False, False, True,  False, False, False, False, False,
                      False, False, False, False, False, False, False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        expected = ["d6", "c6"]
        assert pawn.get_valid_moves("d5", match) == expected


    def test_pawn_en_passant_3(self):
        pawn = PawnPiece()
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
        en_passant = [False, False, False, False, False, False, False, False,
                      False, False, False, True,  False, False, False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        expected = ["e3", "d3"]
        assert pawn.get_valid_moves("e4", match) == expected


    def test_pawn_en_passant_4(self):
        pawn = PawnPiece()
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
        en_passant = [False, False, False, False, False, False, False, False,
                      False, False, False, False, False, True,  False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        expected = ["e3", "f3"]
        assert pawn.get_valid_moves("e4", match) == expected


    def test_pawn_not_en_passant_1(self):
        pawn = PawnPiece()
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
        match = ChessMatch(board)
        expected = ["e6"]
        assert pawn.get_valid_moves("e5", match) == expected


    def test_pawn_not_en_passant_2(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["e6"]
        assert pawn.get_valid_moves("e5", match) == expected


    def test_get_valid_v_moves_none_1(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn._get_valid_v_moves("d5", match) == expected
        

    def test_get_valid_v_moves_none_2(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert pawn._get_valid_v_moves("c3", match) == expected


    def test_get_valid_v_moves_1(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -3,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d4"]
        assert pawn._get_valid_v_moves("c3", match) == expected
        
        
    def test_get_valid_v_moves_2(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  0,  2,  4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f5"]
        assert pawn._get_valid_v_moves("e6", match) == expected


    def test_get_valid_v_moves_3(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  0,  0,  0,
             0,  0,  0,  2,  2,  4,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d5", "f5"]
        assert pawn._get_valid_v_moves("e6", match) == expected
    
    
    def test_get_valid_v_moves_4(self):
        pawn = PawnPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0, -4,  2, -3,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c4", "e4"]
        assert pawn._get_valid_v_moves("d3", match) == expected




















































































































































































































