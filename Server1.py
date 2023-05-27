# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:03:30 2023

@author: Mariam
"""

from socket import *
import json
import random

SERVER = "Mariam_Server"
LISTNER_PORT = 63777

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', LISTNER_PORT))

while True:
    
    server_socket.listen()
    client = server_socket.accept()[0]
    client_ = client.recv(1024).decode()
    
    parsed_data = json.loads(client_)
    
    # Check again from server-side the input number of the user is valid
    if parsed_data["number"] > 100 or parsed_data["number"] < 1:
        break
    
    print(f'Client Name: {parsed_data["name"]} - Server Name: {SERVER}')
    
    # Serve get a random number from 1 to 100
    serverNO = random.randint(1, 100)

    print(f'Client Number: {parsed_data["number"]}\nServer Number: {serverNO}\nSum: {parsed_data["number"] + serverNO}')

    sum_ = serverNO + parsed_data["number"]

    client.send(json.dumps({"server_number": serverNO, "server_name": SERVER}).encode())

client.close()