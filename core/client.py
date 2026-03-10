import socket
import threading
from utils.constants import PORT, BUFFER_SIZE
from core.message_protocol import create_message, parse_message

class ChatClient:
    def __init__(self, host_ip, username, gui_callback):
        self.host_ip = host_ip
        self.username = username
        self.gui_callback = gui_callback
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client.connect((self.host_ip, PORT))
            self.client.send(create_message("join", self.username))
            threading.Thread(target=self.receive, daemon=True).start()
        except:
            self.gui_callback("error", "Connection failed")

    def receive(self):
        while True:
            try:
                data = self.client.recv(BUFFER_SIZE)
                message = parse_message(data)

                if message["type"] == "accept":
                    self.gui_callback("info", "Connected")
                elif message["type"] == "reject":
                    self.gui_callback("error", "Rejected by host")
                    self.client.close()
                elif message["type"] == "chat":
                    self.gui_callback(
                        "chat",
                        f"{message['username']}: {message['message']}"
                    )
                elif message["type"] == "system":
                    self.gui_callback("chat", message["message"])
            except:
                break

    def send_message(self, text):
        self.client.send(
            create_message("chat", self.username, text)
        )