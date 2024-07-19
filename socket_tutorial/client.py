import socket
import connection_consts as consts


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(consts.get_address())
    
    connected = True

    while connected:
        message = input("Say something to the server: ")
        send(message, client)

        print(client.recv(2048).decode(consts.get_encoder_format()))

        if message == consts.DISCONNECT_MESSAGE:
            connected = False


def send(message, client):
    format = consts.get_encoder_format()
    header = consts.get_header()
    encoded_message = message.encode(format)
    send_length = str(len(encoded_message)).encode(format)
    # Add padding for header
    send_length += b' ' * (header - len(send_length))
    client.send(send_length + encoded_message)
    
    
def get_all_messages(client):
    pass
    #client.recv()


if __name__ == "__main__":
    main()
