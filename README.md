# Secure P2P LAN Chat System

A Python-based Peer-to-Peer LAN Chat Application that allows multiple users to communicate in the same network without using a central server.

## Features

- Peer-to-Peer architecture
- UDP socket communication
- GUI interface using Tkinter
- Multi-user chat support
- Modular project structure

## Project Structure

Secure-P2P-LAN-Chat
│
├── core
│   ├── client.py
│   ├── server.py
│   ├── connection_manager.py
│   └── message_protocol.py
│
├── gui
│   ├── client_gui.py
│   └── host_gui.py
│
├── utils
│   ├── constants.py
│   └── network_utils.py
│
├── main_client.py
├── main_host.py
└── requirements.txt

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Application

Start Host:

python main_host.py

Start Client:

python main_client.py