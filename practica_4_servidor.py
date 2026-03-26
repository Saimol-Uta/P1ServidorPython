import socket
import threading

HOST = "10.53.25.239"
PORT = 5000
BUFFER_SIZE = 1024
BACKLOG = 10


def atender_cliente(conexion, addr):
    """Atiende a un cliente, recibe su mensaje y responde confirmacion."""
    with conexion:
        try:
            print(f"Cliente conectado desde: {addr}")
            data = conexion.recv(BUFFER_SIZE)

            if not data:
                print(f"Conexion cerrada sin datos por {addr}")
                return

            mensaje = data.decode("utf-8", errors="replace")
            print(f"Datos recibidos de {addr}: {mensaje}")

            respuesta = f"Hola cliente, {addr}, mensaje recibido"
            conexion.sendall(respuesta.encode("utf-8"))
        except ConnectionResetError:
            print(f"Conexion reiniciada por el cliente {addr}")
        except OSError as error:
            print(f"Error de socket con {addr}: {error}")


def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen(BACKLOG)
        print(f"Servidor escuchando en {HOST}:{PORT}")

        while True:
            conexion, addr = server.accept()
            hilo = threading.Thread(
                target=atender_cliente,
                args=(conexion, addr),
                daemon=True,
            )
            hilo.start()
    except KeyboardInterrupt:
        print("\nServidor detenido por teclado")
    except OSError as error:
        print(f"Error en el servidor: {error}")
    finally:
        server.close()
        print("Socket del servidor cerrado")


if __name__ == "__main__":
    iniciar_servidor()