import socket


HEADER = 16
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def get_header():
    return HEADER


def get_port():
    return PORT


def get_server_ip():
    return socket.gethostbyname(socket.gethostname())


def get_address():
    return (get_server_ip(), PORT)


def get_encoder_format():
    return FORMAT


def get_disconnect_message():
    return DISCONNECT_MESSAGE
