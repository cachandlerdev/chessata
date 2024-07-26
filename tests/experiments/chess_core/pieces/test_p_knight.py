from src.experiments.chess_core.game_mode.match_chess import ChessMatch
from src.experiments.chess_core.pieces.p_knight import KnightPiece

class TestKnightPiece:

    def test_get_valid_moves_1(self):
        knight = KnightPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  3,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c5", "d6", "f6", "g5", "g3", "f2", "d2", "c3"]
        assert knight.get_valid_moves("e4", match) == expected
        
        
    def test_get_valid_moves_2(self):
        knight = KnightPiece()
        board = [
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["h7", "g6", "e6", "d7"]
        assert knight.get_valid_moves("f8", match) == expected
    
    
    def test_get_valid_moves_3(self):
        knight = KnightPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            -3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b7", "c6", "c4", "b3"]
        assert knight.get_valid_moves("a5", match) == expected
    
    
    def test_get_valid_moves_4(self):
        knight = KnightPiece()
        board = [
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  3,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  1,  1,
            ]
        match = ChessMatch(board)
        expected = []
        assert knight.get_valid_moves("e4", match) == expected













































