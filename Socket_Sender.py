import socket

print("Client")

socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_main.connect(('localhost', 9999))

while True:
    message = input(": ")
    socket_main.send(message.encode())

socket_main.close()