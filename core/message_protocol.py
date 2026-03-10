import json

def create_message(msg_type, username="", message=""):
    return json.dumps({
        "type": msg_type,
        "username": username,
        "message": message
    }).encode()

def parse_message(data):
    return json.loads(data.decode())