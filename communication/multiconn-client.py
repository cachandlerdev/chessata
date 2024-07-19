#!/usr/bin/env python3

import sys
import socket
import selectors
import types

def main():
    sel = selectors.DefaultSelector()
    messages = [b"Message 1 from client.", b"Message 2 from client."]
    
    
if __name__ == "__main__":
    main()

