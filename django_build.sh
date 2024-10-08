#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
python ./src/web/chess_web/manage.py makemigrations chess_api
python ./src/web/chess_web/manage.py migrate