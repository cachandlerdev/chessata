#!/usr/bin/env python3

import socket


def main():
    # Standard loopback interface address (localhost)
    HOST = "127.0.0.1"
    
    # Port to listen on (non-privileged ports are > 1023)
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


if __name__ == "__main__":
    main()