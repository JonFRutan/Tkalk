import tkinter as tk
from modules.Connector import ClientConnector
from modules.UI import ClientUI

class ClientApp:
    def __init__(self):
        self.connection = ClientConnector()
