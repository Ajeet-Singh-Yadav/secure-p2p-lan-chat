import socket
import threading
from utils.constants import PORT, BUFFER_SIZE
from core.connection_manager import ConnectionManager
from core.message_protocol import create_message, parse_message

class ChatServer:
    def __init__(self, gui_callback):
        self.host = "0.0.0.0"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, PORT))
        self.server.listen()
        self.manager = ConnectionManager()
        self.gui_callback = gui_callback
        self.running = True

    def start(self):
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        while self.running:
            client, addr = self.server.accept()

            data = client.recv(BUFFER_SIZE)
            message = parse_message(data)

            if message["type"] == "join":
                username = message["username"]

                allow = self.gui_callback("approve", username)

                if not allow:
                    client.send(create_message("reject"))
                    client.close()
                    continue

                client.send(create_message("accept"))
                self.manager.add_client(client, username)

                self.manager.broadcast(
                    create_message("system", message=f"{username} joined")
                )

                threading.Thread(
                    target=self.handle_client,
                    args=(client,),
                    daemon=True
                ).start()

    def handle_client(self, client):
        while self.running:
            try:
                data = client.recv(BUFFER_SIZE)
                if not data:
                    break

                message = parse_message(data)

                if message["type"] == "chat":
                    self.manager.broadcast(
                        create_message(
                            "chat",
                            message["username"],
                            message["message"]
                        )
                    )
            except:
                break

        username = self.manager.remove_client(client)
        if username:
            self.manager.broadcast(
                create_message("system", message=f"{username} left")
            )
        client.close()

    def stop(self):
        self.running = False
        self.server.close()