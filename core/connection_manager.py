class ConnectionManager:
    def __init__(self):
        self.clients = []
        self.usernames = []

    def add_client(self, client, username):
        self.clients.append(client)
        self.usernames.append(username)

    def remove_client(self, client):
        if client in self.clients:
            index = self.clients.index(client)
            self.clients.remove(client)
            username = self.usernames.pop(index)
            return username
        return None

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)