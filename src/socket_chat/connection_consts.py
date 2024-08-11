import socket


HEADER = 16
MESSAGE_SIZE = 2048
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def get_server_ip():
    return socket.gethostbyname(socket.gethostname())


def get_address():
    return (get_server_ip(), PORT)