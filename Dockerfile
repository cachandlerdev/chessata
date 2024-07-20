FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app/chess_core
RUN pip install -r ../requirements.txt
CMD ["python3", "chess_main.py"]