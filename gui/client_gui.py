import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
from core.client import ChatClient

class ClientGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Client - P2P Chat")

        self.chat_area = scrolledtext.ScrolledText(self.window)
        self.chat_area.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.send_button = tk.Button(
            self.window,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack()

        host_ip = simpledialog.askstring("Host IP", "Enter Host IP:")
        username = simpledialog.askstring("Username", "Enter Username:")

        self.client = ChatClient(host_ip, username, self.gui_callback)
        self.client.connect()

    def gui_callback(self, action, data):
        if action == "chat":
            self.chat_area.insert(tk.END, data + "\n")
        elif action == "error":
            messagebox.showerror("Error", data)
        elif action == "info":
            messagebox.showinfo("Info", data)

    def send_message(self):
        text = self.entry.get()
        self.client.send_message(text)
        self.entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()