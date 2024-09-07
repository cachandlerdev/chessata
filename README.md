# Chessata
A chess website you can use to play online with your friends!

![Logo](/src/web/chess_web/frontend/src/assets/dashboard_logo.png)

## Screenshots
TODO: Add 2-3 screenshots here

## Current website
TODO: Add the website link here

## Distinctiveness and Complexity (CS50W)
TODO: Add this stuff for CS50W. (Don't worry, you'll probably end up deleting it after the project gets graded).

## Development
This is a multiplayer network-based full stack chess application that uses a React frontend to make API calls to a Django backend over the WebSockets protocol.
We accomplish this using Django Channels and its Daphne server, and tests are run via Pytest and Selenium.
Redis is utilized in order to make use of channel layers and store information.
This allows us to perform real time updates with low server overhead via JSON responses as described in the [API Documentation](api_documentation.md). 

### Installation
TODO: Add instructions on how to run things locally and install dependencies.

### Running the Web App

1. First spin up the Redis database.
    - Run `docker run -p 6379:6379 -d redis:5`
2. Next startup the backend:
    - Navigate to `src/web/chess_web`.
    - Run `python manage.py runserver`.
3. Then startup the frontend:
    - Open a new terminal.
    - Navigate to `src/web/chess_web/frontend`.
    - Run `npm start`.

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