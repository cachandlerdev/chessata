from game_mode.match_chess import ChessMatch


def main():
    """A console based client for the chess module designed for simple testing
    purposes."""
    print("Welcome to Chessole, my console based chess tester application!")
    run_app()


def run_app():
    """The main application loop.."""
    game_number = 1
    keep_running = True
    while keep_running:
        play_match(game_number)

        print("-----------------------------")
        answer = input("Play again? (Y/N): ")
        if answer.lower() == "n":
            keep_running = False
        else:
            game_number += 1


def play_match(game_number):
    """Plays out a chess match."""
    chess_match = ChessMatch()
    draw_match(chess_match)

    # draw it visually
    # Starts as white's turn
    # Player makes move
    # Update match state 
    # Update turn to be black
    # Redraw visually



def draw_match(match):
    """Draws the game board."""
    print("BOARD GOES HERE")

    

if __name__ == "__main__":
    main()