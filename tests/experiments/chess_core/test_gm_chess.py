from src.experiments.chess_core.game_mode.gm_chess import ChessGameMode


def test_is_not_three():
    mode = ChessGameMode()
    assert mode.is_three(4) == False


def test_is_three():
    mode = ChessGameMode()
    assert mode.is_three(3) == True
