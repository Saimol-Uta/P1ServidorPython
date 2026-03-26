import socket
import threading
HOST = '10.79.10.120'
PORT = 5000

def cliente(id_cliente):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    mensaje = f"Saimol Jimenez Cliente {id_cliente} conectado"
    s.send(mensaje.encode())

    respuesta = s.recv(1024).decode()
    print(f"Cliente {id_cliente} recibe {respuesta}")
    s.close()

hilos = []
for i in range(1):
    hilo = threading.Thread(target=cliente, args=(i,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()