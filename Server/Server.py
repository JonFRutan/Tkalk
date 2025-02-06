import re, sys
import threading
import socket
from modules import *

args = sys.argv
if len(args) > 1:
    port_number = int(args[1])
else: 
    print("Usage: \n> python3 Server.py port")
    print("*Remember to use a port of at least 4 digits*")
    exit()

def handle_client(connection_socket, addr):
    print(f"Client connected from {addr}")
    client_connected = True
    while client_connected:
        try:
            data = connection_socket.recv(1024).decode()
            if not data:
                 break
            print(f"From {addr}: {data}")
            connection_socket.sendall("Message received".encode())
        except:
            print(f"Error in handle_client at try block.")
            break
    print(f"Client {addr} disconnected")
    connection_socket.close()
    
init_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname_ex(socket.gethostname())[2][0]  # Gets the first IP
init_socket.bind((host, port_number))
init_socket.listen()
print(f"Listening at {host}:{port_number}...")

running = True
while running:
    connection_socket, addr = init_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection_socket, addr))
    client_thread.start()