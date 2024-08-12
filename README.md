# Instructions for testing the core chess functionality

In order to run `chess_full_client.py`, you need to be in the `src` folder and run `python -m chess_core.chess_full_client` (without the `.py`!). If you try to run it directly from `chess_core`, you will get errors. This is because of an annoying issue with relative imports and launching as a module vs a script.

Also note that all imports in the `tests` folder need to start at `src.otherstuff`. This is because of some issue with Pytest that I don't want to worry about right now.