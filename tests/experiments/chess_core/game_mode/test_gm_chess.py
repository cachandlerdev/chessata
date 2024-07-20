from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode

class TestChessGameMode:

    def test_is_not_three(self):
        mode = ChessGameMode()
        assert mode.is_three(4) == False


    def test_is_three(self):
        mode = ChessGameMode()
        assert mode.is_three(3) == True


    def test_true(self):
        assert True