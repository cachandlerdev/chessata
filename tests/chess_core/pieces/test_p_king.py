import pytest
from src.chess_core.pieces.p_king import KingPiece
from src.chess_core.game_mode.match_chess import ChessMatch


class TestKingPiece:
    
    def test_get_valid_moves_no_piece(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        with pytest.raises(ValueError, match="Piece not found."):
            king.get_valid_moves("d5", match)


    def test_get_valid_moves_right_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  6,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["e5"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_valid_moves_left_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  6,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c5"]
        assert king.get_valid_moves("d5", match) == expected
    

    def test_get_valid_moves_up_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  0,  2,  0,  0,
             0,  0,  0,  1,  6,  3,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["e2"]
        assert king.get_valid_moves("e1", match) == expected
    
    
    def test_get_valid_moves_down_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1, -1, -1,  0,
             0,  0,  0,  0, -1, -6, -4,  0,
             0,  0,  0,  0, -2,  0, -3,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["f4"]
        assert king.get_valid_moves("f5", match) == expected
    
    
    def test_get_valid_moves_up_right_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  0,  0,  0,  0,
             0,  0,  1,  6,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["e6"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_valid_moves_up_left_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  1,  0,  0,  0,
             0,  0,  1,  6,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c6"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_valid_moves_down_left_only(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  1,  6,  1,  0,  0,  0,
             0,  0,  0,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c4"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_two_valid_moves_1(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  1,  0,  0,  0,
             0,  0,  1,  6,  1,  0,  0,  0,
             0,  0,  0,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["c6", "c4"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_two_valid_moves_2(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  0,  0,  0,  0,  0,
             0,  0,  1,  6,  1,  0,  0,  0,
             0,  0,  1,  1,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d6", "e6"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_three_valid_moves_1(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  1,  0,  1,  0,  0,  0,
             0,  0,  0,  6,  1,  0,  0,  0,
             0,  0,  1,  1,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d6", "c5", "e4"]
        assert king.get_valid_moves("d5", match) == expected
    
    
    def test_get_three_valid_moves_2(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  1,  1,  0,  0,  0,
             0,  0,  1,  6,  0,  0,  0,  0,
             0,  0,  1,  0,  1,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d4", "e5", "c6"]
        assert king.get_valid_moves("d5", match) == expected
        

    def test_get_valid_moves_all_dirs(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d6", "d4", "c5", "e5", "c6", "e6", "c4", "e4"]
        assert king.get_valid_moves("d5", match) == expected
        
        
    def test_get_valid_moves_left_edge(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0, -1,  0,  0,  0,  0,  0,  0,
            -6,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["a6", "a4", "b5", "b4"]
        assert king.get_valid_moves("a5", match) == expected
        
        
    def test_get_valid_moves_top_edge(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  6,  2,  0,  0,
             0,  0,  0,  3,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["e7", "d8", "f7"]
        assert king.get_valid_moves("e8", match) == expected
        
        
    def test_get_valid_moves_right_edge(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  5,  0,
             0,  0,  0,  0,  0,  0,  0,  6,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["h6", "h4", "g5", "g4"]
        assert king.get_valid_moves("h5", match) == expected
        
        
    def test_get_valid_moves_bottom_edge(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["d2", "c1", "e1", "c2", "e2"]
        assert king.get_valid_moves("d1", match) == expected
        
         
    def test_get_valid_moves_top_left_corner(self):
        king = KingPiece()
        board = [
            -6,  0,  0,  0,  0,  0,  0,  0,
             0, -2,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["a7", "b8"]
        assert king.get_valid_moves("a8", match) == expected
        
        
    def test_get_valid_moves_top_right_corner(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  1,  6,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  6,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["h7", "g7"]
        assert king.get_valid_moves("h8", match) == expected
        
        
    def test_get_valid_moves_bottom_left_corner(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             6,  0,  0,  6,  0,  0,  0,  0,
            ]
        match = ChessMatch(board)
        expected = ["a2", "b1", "b2"]
        assert king.get_valid_moves("a1", match) == expected
        
        
    def test_get_valid_moves_bottom_right_corner(self):
        king = KingPiece()
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  5,  6,
            ]
        match = ChessMatch(board)
        expected = ["h2", "g2"]
        assert king.get_valid_moves("h1", match) == expected
