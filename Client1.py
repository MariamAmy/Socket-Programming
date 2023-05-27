# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:12:19 2023

@author: Mariam
"""

from socket import *
import json

# Specify serve name and port number
server_name = 'localhost'
server_port = 63777
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_name, server_port))

# Take user input
clientName = input("Enter your Name:\n")
clientNumber = int(input("Input number between 1 and 100:\n"))

# Encode client's data , name and number, and send them to the server
data = {"name": clientName, "number": clientNumber}
jsonData = json.dumps(data).encode()
clientSocket.send(jsonData)

#Check the user number in range from 1 to 100
if clientNumber > 100 or clientNumber < 1:
    clientSocket.close()
else:
    response = clientSocket.recv(1024).decode()
    parsedResponse = json.loads(response)
    
    #print(parsedResponse)
    print("Client Name: ", clientName, " || Server Name: ", parsedResponse["server_name"], " || Server Number: ", parsedResponse["server_number"])
    clientSocket.close()