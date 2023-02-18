import socket

print("Host")

socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_main.bind(('localhost', 9999))

socket_main.listen(1)
conn, addr = socket_main.accept()

while True:
    data = conn.recv(1204).decode()
    print(data)

conn.close()