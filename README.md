# Chessata
A chess website you can use to play online with your friends!

![Logo](/src/web/chess_web/frontend/src/assets/dashboard_logo.png)

## Screenshots

![Dashboard](/screenshots/dashboard.png)
![Logo](/screenshots/game_desktop.png)

## Distinctiveness and Complexity
I've always wanted to make a Chess website.
It's such an elegant game, this two-player ruleset with virtually infinite complexity and variability between matches without any reliance on dice rolls or other forms of randomness.
With such a rich history involving centuries of strategy refinement and academic study, as well as an incredibly in-depth collection of moves that build upon each other, how could it not fascinate the aspiring software developer, keen to apply his recently acquired theoretical knowledge in the realm of computer science to the test?

Indeed, from a programming standpoint, chess is quite an interesting combination of challenges to be solved.
The designer must consider how to programmatically represent the board and its various pieces, how to predict possible moves for each piece type, and how to determine win conditions for a given chess board.
The task initially appears fairly simplistic, but becomes increasingly complex when he realizes that the program must be able to recognize less common moves such as *en passant* attacks from pawns, *castling* moves involving the king and his rooks, and piece *promotions*.
And, keep in mind, this is without even considering the additional complexity introduced by the inclusion of a graphical interface, or without thinking about how the programmer might handle input from multiple players over the internet.  
If he were to delve into those weeds, it would be incredibly easy to lose the forest for the trees upon learning about networking concepts like HTTP requests, Websockets, or internet protocols, or when thinking about how one might visually display the game board to users and dynamically update it when moves are made.

As such, when I decided to begin working on this project, I had to do what every programmer does when presented with a large problem: break things down into simpler challenges that can be addressed individually, test them, and expand from there.

### "Chessole"
Given the inherent complexity in designing a chess program on its own as demonstrated above, I decided to begin with a text-based console application.
Hence, Chessata began its life as a collection of `ChessGameMode` functions inside a `chess_core` module evaluated using Pytest.
In time, this humble module expanded to include `ChessMatch`, a class designed to track the state of a board, `BasePiece` and its children, which became critical in calculating the available moves for individual game pieces, and some other odds and ends that came together to form the backbone of my chess engine.

From there, it was time to put the little module to a test, and so I wrote `chess_full_client.py`, a simple console application dubbed "Chessole" that processes input from two users at the same computer and called the corresponding engine commands.

![Chessole: A text based rudimentary chess program](/screenshots/chessata_console.png)

### Clients, Servers, and Frontends
After getting this far, it was time to hit the books and start learning about networking.
I won't bore you with the details I learned about the differences between TCP and UDP protocols, or the UNIX `socket` API, but suffice to say that this was an informative process that taught me a great deal about how information routes from one device to another across the globe on the modern Internet, and it gave me the necessary knowledge to continue working on my chess website.

During this time, I ended up creating a number of multi-user chat applications at various abstraction levels, from the barebones Python `socket` library where I was manually encoding and decoding data packets sent between clients and servers, to higher level versions of the same concept involving the `websockets` library, and finally once more at the Django Channels level.

### The Web Application
From there, given that it was not realistically feasible to design a real-time multiplayer game using server-side rendering, I began learning about React, one of the most popular frontend frameworks in modern web development, and how it could be integrated into a Django application.
Traditionally, this would be accomplished using the Django REST Framework, but given that I was using the Websocket protocol to reduce communication overhead and improve efficiency, I ended up developing a custom JSON API that you can learn about in greater detail [here](api_documentation.md).

As for how exactly I accomplished this, most of the backend logic occurs in the `src/web/chess_web/chess_api/` folder inside `consumers.py`, where my `ClientConsumer` class processes Websocket communication requests with the help of `chess_manager.py` and `lobby_manager.py`, and stores information about users and chess matches as needed inside an SQLite or Postgresql database (SQLite is used locally, but Postgresql is also supported for use with server hosting websites).
This backend then talks to my React frontend, located at `src/web/chess_web/frontend`, which processes user input and displays matches in a visually appealing and responsive web layout that allows users to host, join, or spectate game lobbies, play chess matches, and chat with each other over text.

All in all, this was a very large project that took a great deal of time to research, design, and implement, and it was a large step up in complexity from the simpler server-side Django applications I had been learning how to make in the past with CS50W.
Overall however, the end result was definitely worth it, and while I obviously have no plans to compete with the likes of Chess.com and Lichess for the time being, I would argue that my application could be considered more aesthetically pleasing than its competitors. 😉

## For Developers
This is a multiplayer network-based full stack chess application that uses a React frontend to make API calls to a Django backend over the WebSockets protocol.
We accomplish this using Django Channels and its Daphne server, and tests are run via Pytest and Selenium.
Redis is utilized in order to make use of channel layers and store information.
This allows us to perform real time updates with low server overhead via JSON responses as described in the [API Documentation](api_documentation.md). 

### Installation

1. First install the backend Django dependencies 
    - Navigate to the root directory.
    - Run `pip install -r requirements.txt`.
        - I recommend using a virtual environment (`venv`).
2. Then install the dependencies for the React frontend.
    - Navigate to `src/web/chess_web/frontend/`.
    - Run `npm install` to download all of the packages located in `package.json`.
3. Lastly, you'll have to install [Docker](https://www.docker.com/), which we use to run Redis via the `channels-redis` python library.

### Running the Web App

1. First spin up the Redis database. This facilitates communication between the frontend and backend via websockets.
    - Run `docker run -p 6379:6379 -d redis:5`
2. Next startup the backend:
    - Navigate to `src/web/chess_web`.
    - Run `python manage.py runserver`.
        - If you want to connect to other devices, you have to specify the ip and port (which must be open on the firewall). For example: `python manage.py runserver 192.168.254.155:8000`.
3. Then startup the frontend:
    - Open a new terminal.
    - Navigate to `src/web/chess_web/frontend`.
    - Run `npm start`.
4. Navigate to the address mentioned in the `npm start` terminal. (e.g. `http://localhost:44824/`)

### Running the Console App

You can run the chess terminal application locally with the use of `chess_full_client.py`.
This can be helpful for testing core functionality without needing to worry about the complexities introduced by Django or React.

1. Navigate to `src/`.
    - Make sure you're in the root `src` folder and not `frontend/src/`, which holds the React code.
2. Run `python -m chess_core.chess_full_client`.
    - Don't include `.py` in the command.
    - Don't try to run the script from the `chess_core/` directory, or else you'll run into issues with relative imports and launching the app as a script instead of a module.

### Notes

All imports in the `tests` folder need to start at `src.otherstuff`.
This occurs due to an issue that Pytest has regarding relative imports.