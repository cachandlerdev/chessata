from src.chess_core.game_mode.match_chess import ChessMatch
from src.chess_core.pieces.p_bishop import BishopPiece


class TestBishopPiece:
    
    def test_get_valid_moves_1(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c6", "b7", "a8", "e6", "f7", "g8", "c4", "b3", "a2", "e4", "f3", "g2", "h1"]
        assert bishop.get_valid_moves("d5", match) == expected
    

    def test_get_valid_moves_2(self):
        bishop = BishopPiece()
        board = [
             3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b7", "c6", "d5", "e4", "f3", "g2", "h1"]
        assert bishop.get_valid_moves("a8", match) == expected


    def test_get_valid_moves_3(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  3,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["g7", "f6", "e5", "d4", "c3", "b2", "a1"]
        assert bishop.get_valid_moves("h8", match) == expected


    def test_get_valid_moves_4(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b2", "c3", "d4", "e5", "f6", "g7", "h8"]
        assert bishop.get_valid_moves("a1", match) == expected


    def test_get_valid_moves_5(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  3,
            ]
        match = ChessMatch(board)
        expected = ["g2", "f3", "e4", "d5", "c6", "b7", "a8"]
        assert bishop.get_valid_moves("h1", match) == expected


    def test_get_valid_moves_collision_1(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  3,
            ]
        match = ChessMatch(board)
        expected = ["g2"]
        assert bishop.get_valid_moves("h1", match) == expected


    def test_get_valid_moves_collision_2(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  4,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             3,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b2", "c3"]
        assert bishop.get_valid_moves("a1", match) == expected


    def test_get_valid_moves_collision_3(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  3,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["g7", "f6", "e5"]
        assert bishop.get_valid_moves("h8", match) == expected


    def test_get_valid_moves_collision_4(self):
        bishop = BishopPiece()
        board = [
             3,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  1,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["b7", "c6", "d5", "e4", "f3"]
        assert bishop.get_valid_moves("a8", match) == expected


    def test_get_valid_moves_collision_5(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  1,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  2,
            ]
        match = ChessMatch(board)
        expected = ["c6", "e6", "c4", "b3", "e4", "f3", "g2"]
        assert bishop.get_valid_moves("d5", match) == expected


    def test_get_valid_moves_collision_6(self):
        bishop = BishopPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  5,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = []
        assert bishop.get_valid_moves("d5", match) == expected
