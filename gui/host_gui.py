import tkinter as tk
from tkinter import scrolledtext, messagebox
from core.server import ChatServer
from utils.network_utils import get_local_ip

class HostGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Host - P2P Chat")

        self.chat_area = scrolledtext.ScrolledText(self.window)
        self.chat_area.pack()

        self.server = ChatServer(self.gui_callback)
        self.server.start()

        ip = get_local_ip()
        self.chat_area.insert(tk.END, f"Room started at IP: {ip}\n")

        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def gui_callback(self, action, data):
        if action == "approve":
            return messagebox.askyesno("Approval", f"Allow {data}?")
        elif action == "chat":
            self.chat_area.insert(tk.END, data + "\n")

    def close(self):
        self.server.stop()
        self.window.destroy()

    def run(self):
        self.window.mainloop()