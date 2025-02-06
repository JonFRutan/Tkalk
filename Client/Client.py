import tkinter as tk
import socket
from modules.Connector import ClientConnector
from modules.UI import ClientUI

def prompt_user():
    host_ip = input("Server IP: ")
    host_port = input("Server port: ")
    return host_ip, host_port

class ClientApp:
    def __init__(self):
        #FIXME - This obviously needs to be fixed
        connection = None
        #self.connection.connect()
        self.root = tk.Tk()
        self.ui = ClientUI(self.root, connection)

    def run(self):
        self.ui.run()
        #self.connection.close()

if __name__ == "__main__":
    app = ClientApp()
    app.run()
