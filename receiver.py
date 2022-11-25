import os
import socket
import time

host = input("Enter Host Name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This tries to connect to the socket.
try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# Transfers all the details of the file.
Name_Of_File = sock.recv(100).decode()
sizeOfFile = sock.recv(100).decode()

# Opens and reads the file.
with open("./image of nature/" + Name_Of_File, "wb") as file:
    X = 0
    # This line captures the intial time.
    initial_time = time.time()

    # This while loop runs untile the file is received.
    while X <= int(sizeOfFile):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        X = X + len(data)

    # This lines captures the finish time.
    final_time = time.time()

print("File transfer Complete.Total time: ", final_time - initial_time)

# This line closes the socket.
sock.close()