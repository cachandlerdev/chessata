import socket
import threading
import connection_consts as consts

client_list = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address an Errno 98 issue after force quitting
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(consts.get_address())
    
    start(server, consts.get_server_ip(), consts.HEADER)
    
    
def handle_client(client, addr, header):
    print(f"New connection from {addr}.")
    format = consts.FORMAT
    
    connected = True
    while connected:
        msg_length = client.recv(header).decode(format)
        if msg_length:
            # Make sure the response isn't empty
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(format)
            print(f"[{addr}]: {msg}")
            
            for idx, conn in enumerate(client_list):
                if conn != client:
                    message_client(conn, f"[User {idx + 1}]: {msg}")
            #client.send(f"New Message: {msg}".encode(format))

            if msg == consts.DISCONNECT_MESSAGE:
                connected = False
    
    client.close()


def message_client(client, message):
    format = consts.FORMAT
    header = consts.HEADER
    encoded_message = message.encode(format)
    send_length = str(len(encoded_message)).encode(format)
    # Add padding for header
    send_length += b' ' * (header - len(send_length))
    client.send(send_length + encoded_message)


def start(server, server_ip, header):
    server.listen()
    print(f"Server is listening on {server_ip}")
    while True:
        client, addr = server.accept()
        client_list.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr, header))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


if __name__ == "__main__":
    main()