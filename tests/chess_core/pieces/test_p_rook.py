from src.chess_core.game_match.match_chess import ChessMatch
from src.chess_core.pieces.p_rook import RookPiece


class TestRookPiece:
    
    def test_get_valid_vertical_moves_1(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  2,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d6", "d7", "d8", "d4", "d3", "d2", "d1"]
        assert rook.get_valid_moves("d5", match) == expected
    
    
    def test_get_valid_vertical_moves_2(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1, -2, -3,
            ]
        match = ChessMatch(board)
        expected = ["g2", "g3", "g4", "g5", "g6", "g7", "g8"]
        assert rook.get_valid_moves("g1", match) == expected
    
    
    def test_get_valid_vertical_moves_3(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  3,  2,  1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f7", "f6", "f5", "f4", "f3", "f2", "f1"]
        assert rook.get_valid_moves("f8", match) == expected


    def test_get_valid_vertical_moves_collision_1(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  3,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  2,  4,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b3", "b4", "b1"]
        assert rook.get_valid_moves("b2", match) == expected


    def test_get_valid_vertical_moves_collision_2(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  2,  1,  0,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d7", "d8"]
        assert rook.get_valid_moves("d6", match) == expected
    
    
    def test_get_valid_vertical_moves_collision_3(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1, -2, -1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f6", "f4"]
        assert rook.get_valid_moves("f5", match) == expected
        
        
    def test_get_valid_vertical_moves_collision_4(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             5,  1,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert rook.get_valid_moves("a5", match) == expected

    
    def test_get_valid_moves_1(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d6", "d7", "d8", "d4", "d3", "d2", "d1", "c5", "b5", "a5", "e5", "f5", "g5", "h5"]
        assert rook.get_valid_moves("d5", match) == expected


    def test_get_valid_moves_2(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0, -1,  0,
             0,  0,  0,  0,  0,  0, -2,  0,
            ]
        match = ChessMatch(board)
        expected = ["f1", "e1", "d1", "c1", "b1", "a1", "h1"]
        assert rook.get_valid_moves("g1", match) == expected


    def test_get_valid_moves_3(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             2,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b5", "c5", "d5", "e5", "f5", "g5", "h5"]
        assert rook.get_valid_moves("a5", match) == expected


    def test_get_valid_moves_4(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0,  0,  0,  0,  0,  0,  2,
             0,  0,  0,  0,  0,  0,  0,  1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["g5", "f5", "e5", "d5", "c5", "b5", "a5"]
        assert rook.get_valid_moves("h5", match) == expected
    
    
    def test_get_valid_moves_5(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  1,  2,  1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f7", "f6", "f5", "f4", "f3", "f2", "f1"]
        assert rook.get_valid_moves("f8", match) == expected
    


    def test_get_valid_moves_collision_1(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  3,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  2,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b3", "b4", "b1", "c2", "d2", "e2", "f2", "g2", "h2"]
        assert rook.get_valid_moves("b2", match) == expected


    def test_get_valid_moves_collision_2(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  2,  0,  1,  0,  0,
             0,  0,  0,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d7", "d8", "c6", "b6", "a6", "e6"]
        assert rook.get_valid_moves("d6", match) == expected


    def test_get_valid_moves_collision_3(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0, -4,  0, -2,  0, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0, -3,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f6", "f4", "e5", "g5"]
        assert rook.get_valid_moves("f5", match) == expected
    
    
    def test_get_valid_moves_collision_4(self):
        rook = RookPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             2,  2,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert rook.get_valid_moves("a5", match) == expected
    