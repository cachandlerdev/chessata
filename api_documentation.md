# Chessata API Documentation

Our backend uses WebSockets to handle real time communication between clients and the server.
Communication is done via JSON format.

In order to initialize a connection, a client must connect using a particular game code.
The server will then check whether that code is currently in use, and send back information accordingly.
- If the game code is not in use, then a new game will be initialized, and the server will wait for another user to join over that same game code.
- If the game code is in use, but there is only one player in the lobby, then it will connect the other player and start the match.
- If there are already two players in the lobby, the server will allow the client to spectate the in-progress game.

## Match Storage Format

### Board Format
The server exposes boards as a 64-size array of integers, as demonstrated below.
```json
    "board": [
        -2, -3, -4, -5, -6, -4, -3, -2,
        -1, -1, -1, -1, -1, -1, -1, -1,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         1,  1,  1,  1,  1,  1,  1,  1,
         2,  3,  4,  5,  6,  4,  3,  2]
```

In this format, white pieces are positive numbers, black pieces are negative numbers, and empty squares are `0`.

Numerical value translation:
- `6`: King
- `5`: Queen
- `4`: Bishop
- `3`: Knight
- `2`: Rook
- `1`: Pawn

### Additional Game State Information
We keep information about the game state throughout the match in order to handle en passant and castling moves.
These are explained below.
```json
    "allow_en_passant": [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False
    ],
    "has_king_moved": [
        "white": False, 
        "black": False
    ],
    "has_rook_moved": [
        "a1": False,
        "h1": False,
        "a8": False,
        "h8": False
    ]
```
- `allow_en_passant`: This is a 16-size boolean array that represents whether the rearmost pawn located on this column has exposed himself to an en passant attack.
Internally, we perform evaluation logic to handle cases where multiple pawns are located on the same column. 
The first 8 entries represent black pawns, while the second set of 8 hold information about the white pawns.

- `has_king_moved`: This gets used in order to determine whether players can legally perform castling moves, and holds information about the king's movements.

- `has_rook_moved`: This gets used to determine whether players can legally perform castling moves, and holds information about the various rooks' movements.

## Message Payload Format

All communication is done via JSON format over WebSockets.
- TODO: Update the documentation when you're not running on `127.0.0.1` anymore.

### Init
When a client first connects to a server, it will do so with an address like `ws://127.0.0.1:8000/ws/api/barry/32g9y/` for a client with username `barry` trying to connect with a game code of `32g9y`.

In turn, the server will send back a confirmation payload as follows.

Server to client:
```json
{
    "type": "init",
    "user_id": "132fds0958gjfd",
    "role": "spectator",
}
```

If there are `2` players in a lobby and this person's `role` is `player`, this will be followed up with a Start Game payload.

### Error
If the server is unable to process a client request, it will send back an error packet with the following form.

Server to client:
```json
{
    "type": "error",
    "status_code": 406,
    "message": "[Server message here]",
}
```

### Join
The server sends this to other clients in a game lobby when a new client joins over a particular game code.
The `role` will either be `"player"` or `"spectator"` depending on the status of the person joining.

Server to client:
```json
{
    "type": "join",
    "user_id": "132fds0958gjfd",
    "username": "Billy",
    "role": "player",
}
```

### Leave
The server sends this to other clients in a game lobby when an existing client disconnects.
The `role` will either be `"player"` or `"spectator"` depending on the status of the person leaving.

Server to client:
```json
{
    "type": "leave",
    "user_id": "132fds0958gjfd",
    "username": "Billy",
    "role": "spectator",
}
```

If this was a player and the game was not over yet, this packet will be followed up by an End of Game payload.

### Close Lobby
The server sends this to all clients in a game lobby when both actual players have left the game, at which point all spectators will be disconnected and should return to the dashboard.

Server to client:
```json
{
    "type": "close",
    "message": "Both players have left the match."
}
```

### Start Game
If a second player joins a lobby that had only one player and the match has not started, then the server will send all clients the following response.
The `color` will either be `"white"`, `"black"`, or `"undefined"`, depending on the client's role in the match as a player or a spectator.

Server to client:
```json
{
    "type": "start",
    "color": "black",
}
```

After this, a game status payload will be sent.

### Move 
Players can send the server moves with the following format.
The `promotion` key is optional because it will only get used if the move involves a pawn promotion, and the server defaults to queen promotions when not specified.

Client to server:
```json
{
    "type": "move",
    "start": "c2",
    "end": "c3",
    "promotion": "rook", // <- optional
}
```

If this was an invalid move, the server will respond with an error message.
Otherwise, it will send a game status payload.

### Game State
Each turn, the server will send the state of the board and the `id` of the player whose turn it is.
For this reason, clients should hold onto the `id` the server sends them in the Init payload.

Note that the client itself will never send the server its `id`, as that information is stored on the server when the websocket is created.
However, it should be retained in order to inform users on the client's end whether it is their turn or not.

Server to client:
```json
{
    "type": "game_state",
    "player_turn_id": "132fds0958gjfd",
    "board": [
        -2, -3, -4, -5, -6, -4, -3, -2,
        -1, -1, -1, -1, -1, -1, -1, -1,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,
         1,  1,  1,  1,  1,  1,  1,  1,
         2,  3,  4,  5,  6,  4,  3,  2],
    "allow_en_passant": [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False
    ],
    "has_king_moved": [
        "white": False, 
        "black": False
    ],
    "has_rook_moved": [
        "a1": False,
        "h1": False,
        "a8": False,
        "h8": False
    ],
}
```

For an explanation of the board and other details, see [Match Storage Format](#match-storage-format) above.

### Chat
Users have the ability to communicate with each other by sending messages to the server in the following form.

Client to server:
```json
{
    "type": "chat",
    "message": "[Insert message here]",
}
```

The server will then redistribute that message to every client in the lobby like this:

Server to client:
```json
{
    "type": "chat",
    "username": "Billy",
    "message": "Billy says hi",    
}
```

### Note
The server has the ability to send clients alerts in certain cases, like when the black king is in check.

Server to client:
```json
{
    "type": "note",
    "message": "The black king is in check!",
}
```

### End Of Game
When the game is over or when one player disconnects from an in progress game, the server will send a payload like the one below.
The `result` can either be `"white_win"`, `"black_win"`, `"stalemate"`, `"surrender"`, or `"disconnect"`.

Server to client:
```json
{
    "type": "end_of_game",
    "result": "white_win",
    "winner_id": "132fds0958gjfd",
}
```

Once both players have left the match, all remaining spectators will be disconnected to free up the join code for future matches.
