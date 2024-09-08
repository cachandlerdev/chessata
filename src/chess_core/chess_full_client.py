from chess_core import board_utils
from chess_core.structs.game_state import GameState
from .game_mode import gamemode_chess
from .game_match.match_chess import ChessMatch
from .structs.piece_type import PieceType
import os


def main():
    """A console based client for the chess module designed for simple testing
    purposes."""
    print("Welcome to Chessole, my console based chess tester application!")
    # TODO: Add a start menu with options
    run_app()


def run_app():
    """The main application loop."""
    game_number = 1
    keep_running = True
    while keep_running:
        play_match(game_number)

        print("Thanks for playing Chessole!")
        answer = input("Play again? (Y/N): ")
        if answer.lower() == "n" or answer.lower() == "no":
            keep_running = False
        else:
            game_number += 1


def play_match(game_number):
    """Plays out a chess match."""
    chess_match = ChessMatch()
    game_not_over = True
    is_white_turn = True
    alert = ""
    # TODO: Add some kind of ui for setting promotion type
    while game_not_over:
        draw_match(chess_match, game_number, alert)
        alert = ""
        let_player_move(is_white_turn, chess_match)
        is_white_turn = not is_white_turn

        state = gamemode_chess.resolve_game_state(chess_match, is_white_turn, PieceType.QUEEN)
        match state:
            case GameState.NOT_OVER:
                # Keep playing!
                continue
            case GameState.WHITE_CHECK:
                alert = "White is in check!"
            case GameState.BLACK_CHECK:
                alert = "Black is in check!"
            case _:
                print_game_over(state)
                game_not_over = False


def print_game_over(state):
    """Prints a nice game over message and says who won."""
    message = """
       ______                                 ___                           
 .' ___  |                              .'   `.                         
/ .'   \_|  ,--.   _ .--..--.  .---.   /  .-.  \ _   __  .---.  _ .--.  
| |   ____ `'_\ : [ `.-. .-. |/ /__\\  | |   | |[ \ [  ]/ /__\\[ `/'`\] 
\ `.___]  |// | |, | | | | | || \__.,  \  `-'  / \ \/ / | \__., | |     
 `._____.' \'-;__/[___||__||__]'.__.'   `.___.'   \__/   '.__.'[___]    
                                                                        
    """
    print(message)
    match state:
        case GameState.STALEMATE:
            print("Alas, the game has ended in a stalemate. Better luck next time!")
        case GameState.WHITE_WIN:
            print("White won the game!")
        case GameState.BLACK_WIN:
            print("Black won the game!")


def let_player_move(is_white_turn, match):
    """Lets the given player make a chess move in the format "e3 d5"."""
    need_valid_move = True
    
    while need_valid_move:
        if is_white_turn:
            message = "WHITE MOVE: "
        else:
            message = "BLACK MOVE: "

        answer = input(message)
        try:
            move = sanitize_response(answer)
        except ValueError as e:
            print("Error: " + str(e))
            continue
        
        start = move[0]
        end = move[1]
        
        if gamemode_chess.is_players_piece(start, is_white_turn, match.board):
            try:
                # TODO: Add promotion type
                gamemode_chess.move_piece_at_pos(match, start, end, PieceType.QUEEN)
                need_valid_move = False
            except ValueError as e:
                print("Error: " + str(e))   
        else:
            print("Error: Not player piece.")


def sanitize_response(answer):
    """Sanitizes the user input and returns a tuple with the start and end 
    positions."""
    positions = answer.split(" ")
    if len(positions) != 2:
        raise ValueError("Invalid move format.")

    for position in positions:
        position = position.lower()
        if not board_utils.is_valid_pos(position):
            raise ValueError("Invalid position.")
    
    return positions
    

def draw_match(match, game_number, alert):
    """
    Draws the game board.

    ========================================================
    |     ||     |     |     |     |     |     |     |     |
    |  8  ||  R  |  N  |  B  |  Q  |  K  |  B  |  N  |  R  |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  7  ||  P  |  P  |  P  |  P  |  P  |  P  |  P  |  P  |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  6  ||     |     |     |     |     |     |     |     |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  5  ||     |     |     |     |     |     |     |     |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  4  ||     |     |     |     |     |     |     |     |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  3  ||     |     |     |     |     |     |     |     |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  2  ||  p  |  p  |  p  |  p  |  p  |  p  |  p  |  p  |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    |     ||     |     |     |     |     |     |     |     |
    |  1  ||  r  |  n  |  b  |  q  |  k  |  b  |  n  |  r  |
    |_____||_____|_____|_____|_____|_____|_____|_____|_____|
    ========================================================
    | # 1 ||  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |
    ========================================================

    """
    cls()

    print_logo()

    # Header
    print("========================================================")
    
    # Rows
    index = 0
    for row in range (8, 0, -1):
        print("|     ||     |     |     |     |     |     |     |     |")
        info_row = f"|  {row}  ||  "
        for i in range(8):
            piece_value = match.board[index]
            display = get_visual_piece(piece_value)
            info_row += f"{display}  |  "
            index += 1
        print(info_row)
        print("|_____||_____|_____|_____|_____|_____|_____|_____|_____|")

    # Footer
    print("========================================================")
    if game_number > 9:
        print(f"| #{game_number} ||  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |")
    else:
        print(f"| # {game_number} ||  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h  |")
    print("========================================================")
    
    if alert != "":
        print(f"ALERT: {alert}")



def print_logo():
    """Print a nice app logo. Credit to website below (font name Varsity):
    https://patorjk.com/software/taag/#p=testall&f=Stop&t=Chessole
    """
    print("""
   ______  __                                 __         
 .' ___  |[  |                               [  |        
/ .'   \_| | |--.  .---.  .--.   .--.   .--.  | | .---.  
| |        | .-. |/ /__\\( (`\] ( (`\]/ .'`\ \| |/ /__\\ 
\ `.___.'\ | | | || \__., `'.'.  `'.'.| \__. || || \__., 
 `.____ .'[___]|__]'.__.'[\__) )[\__) )'.__.'[___]'.__.' 
          """)


def cls():
    """Clears the console."""
    os.system("cls" if os.name=="nt" else "clear")
    

def get_visual_piece(value):
    """Gets the visual representation of a given board piece."""
    match value:
        case 6:
            return "k"
        case 5:
            return "q"
        case 4:
            return "b"
        case 3:
            return "n"
        case 2:
            return "r"
        case 1:
            return "p"
        case 0:
            return " "
        case -1:
            return "P"
        case -2:
            return "R"
        case -3:
            return "N"
        case -4:
            return "B"
        case -5:
            return "Q"
        case -6:
            return "K"
    

if __name__ == "__main__":
    main()