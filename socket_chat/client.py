import socket
import connection_consts as consts
import threading
import platform_utils

messages = []
connected = True

def main():
    global connected
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(consts.get_address())
    
    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()
    
    while connected:
        redraw_screen()
        message = input("")
        send(client, message)

        if message == consts.DISCONNECT_MESSAGE:
            connected = False


def send(client, message):
    format = consts.FORMAT
    header = consts.HEADER
    encoded_message = message.encode(format)
    send_length = str(len(encoded_message)).encode(format)
    # Add padding for header
    send_length += b' ' * (header - len(send_length))
    client.send(send_length + encoded_message)
    messages.append(f"[Me]: {message}")
    
    
def receive(client):
    """Constantly waiting for the server to send back information."""
    while is_connected():
        format = consts.FORMAT
        message_length = client.recv(consts.HEADER).decode(format)
        if message_length:
            # Make sure the response isn't empty
            message_length = int(message_length)
            message = client.recv(message_length).decode(format)
            messages.append(message)
            redraw_screen()


def redraw_screen():
    platform_utils.clear_screen()
    print("Fancy Chat App v0.2")
    print("-------------------------")
    for message in messages:
        print(message)
    if len(messages) == 0:
        print("No existing messages.")
    print("-------------------------")
    print("Say something: ", end='', flush=True)
    
    
def is_connected():
    return connected


if __name__ == "__main__":
    main()
