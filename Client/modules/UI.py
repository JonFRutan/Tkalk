import tkinter as tk

class ClientUI:
    def __init__(self, root, connection):
        self.root = root
        root.title("Tkalk Client")
        root.geometry("800x500")

        menu_frame = tk.Frame(root, bg="gray", height=1000)
        menu_frame.pack(fill=tk.X, side=tk.BOTTOM)

        #FIXME: Button positions are currently hard coded
        server_button = tk.Button(menu_frame, text="Servers", command=None).grid(column=0, row=0, sticky="w")
        upload_button = tk.Button(menu_frame, text="Upload", command=None).grid(column=1, row=0, sticky="w")
        send_button = tk.Button(menu_frame, text="Send", command=None).grid(column=2, row=0, sticky="w")

        input_field = tk.Entry(menu_frame)
        input_field.grid(row=0, column=3, sticky="ew", padx=10, pady=5)
        menu_frame.columnconfigure(3, weight=1)

        exit_button = tk.Button(menu_frame, text="Exit", command=root.destroy).grid(column=11, row=0, sticky="e")
        settings_button = tk.Button(menu_frame, text="Settings", command=None).grid(column=10, row=0, sticky="e")
    
    #Button functions
    def send_click(self):
        #Connect to send_button
        pass
    def settings_click(self):
        #Connect to settings_button
        pass
    def upload_click(self):
        #Connect to upload_button
        pass
    def run(self):
        self.root.mainloop()
