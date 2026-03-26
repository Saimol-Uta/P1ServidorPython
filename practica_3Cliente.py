import socket

HOST = "localhost"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("Hola servidor XD".encode())

respuesta = client.recv(1024)
print("Respuesta del servidor:", respuesta.decode())

client.close()