from src.chess_core.game_mode.match_chess import ChessMatch


class TestMatch:
    def test_initial_board_state(self):
        match = ChessMatch()
        expected = [
            -2, -3, -4, -5, -6, -4, -3, -2,
            -1, -1, -1, -1, -1, -1, -1, -1,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             1,  1,  1,  1,  1,  1,  1,  1,
             2,  3,  4,  5,  6,  4,  3,  2,
            ]
        assert match.board == expected


    def test_is_valid_en_passant_1(self):
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
        assert match.is_exposed_to_en_passant("f5") is True
    

    def test_is_valid_en_passant_2(self):
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
        assert match.is_exposed_to_en_passant("c5") is True
    
    
    def test_is_valid_en_passant_3(self):
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
        assert match.is_exposed_to_en_passant("d4") is True
    
    
    def test_is_valid_en_passant_4(self):
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
        assert match.is_exposed_to_en_passant("f4") is True
    
    
    def test_is_valid_en_passant_5(self):
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0, -1,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        en_passant = [False, False, False, False, False, False, False, False,
                      False, False, False, False, False, True,  False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        assert match.is_exposed_to_en_passant("f4") is True
    
    
    def test_is_not_valid_en_passant_1(self):
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
        assert match.is_exposed_to_en_passant("f5") is False
    
    
    def test_is_not_valid_en_passant_2(self):
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
        assert match.is_exposed_to_en_passant("d5") is False
    
    
    def test_is_not_valid_en_passant_3(self):
        board = [
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0, -1,  1,  0,  0,
             0,  0,  0,  0,  0,  1,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            ]
        en_passant = [False, False, False, False, False, False, False, False,
                      False, False, False, False, False, True,  False, False]
        match = ChessMatch(board, allow_en_passant=en_passant)
        assert match.is_exposed_to_en_passant("f4") is False
    
        
