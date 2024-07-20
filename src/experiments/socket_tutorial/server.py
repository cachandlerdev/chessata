import socket
import threading
import connection_consts as consts

all_messages = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(consts.get_address())
    
    print("START SERVER")
    start(server, consts.get_server_ip(), consts.get_header())
    
    
def handle_client(conn, addr, header):
    print(f"New connection from {addr}.")
    
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(consts.get_encoder_format())
        if msg_length:
            # Make sure the response isn't empty
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(consts.get_encoder_format())
            if msg == consts.get_disconnect_message():
                connected = False

            print(f"[{addr}]: {msg}")
            all_messages.append(msg)
            conn.send(f"New Message: {msg}".encode(consts.get_encoder_format()))
    
    conn.close()


def start(server, server_ip, header):
    server.listen()
    print(f"Server is listening on {server_ip}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, header))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


if __name__ == "__main__":
    main()