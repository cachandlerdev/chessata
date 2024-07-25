from src.experiments.chess_core.pieces.p_pawn import PawnPiece


class TestPawnPiece:
    
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
        expected = ["d3", "d4"]
        assert pawn.get_valid_moves("d2", board) == expected