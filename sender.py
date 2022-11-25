import os
import socket
import time

# Creation of socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 22222))
sock.listen(5)
print("Enter the Host Name: ", sock.getsockname())

# This line accepts the connection
client, addr = sock.accept()

# Acquiring the file details.
Name_Of_File = input("Give the File Name: ")
sizeOfFile = os.path.getsize(Name_Of_File)


client.send(Name_Of_File.encode())  # transferring  Name_Of_file and details of it.
client.send(str(sizeOfFile).encode())


with open(Name_Of_File, "rb") as file: # Opens a file and transfers the data.
    X = 0
    
    intial_time = time.time() # The code starts to capture the time

    # Running while loop for c != sizeOFFile
    while X <= sizeOfFile:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        X = X + len(data)

    
    finish_time = time.time() # This ends the capturing of time

print("File Transfer Complete.Total time: ", finish_time - intial_time)

sock.close() # This line closes the socket