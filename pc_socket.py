#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:28:37 2025

@author: edwar
"""


import socket

# Server configuration
SERVER_IP = '192.168.187.215'  # Replace with the server's IP address
PORT = 2024              # Port to connect to (same as the server's PORT)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_IP, PORT))
    print(f"Connected to server at {SERVER_IP}:{PORT}")

    while True:
        # Get input from the user
        message = input("Digite o 'exit' para salir): ")
        if message.lower() == 'exit':
            print("Closing connection...")
            break

        # Send the message
        client_socket.sendall(message.encode('utf-8'))
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client_socket.close()

 
