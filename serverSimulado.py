import socket
import threading

HOST = '10.53.25.239'
PORT = 8086

def manejar_cliente(conexion, direccion):
    print(f"Cliente conectado desde: {direccion}")
    
    request = conexion.recv(1024).decode(errors="ignore")
    print(f"Mensaje recibido de {direccion}: {request}")
    print(request)

    body = """<!doctype html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Servidor Simulado</title>
    <style>
        :root {
            --fondo: #f4f1ea;
            --panel: #fffdf8;
            --texto: #1f2937;
            --detalle: #9a3412;
            --borde: #e7dfd2;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            font-family: Georgia, Cambria, \"Times New Roman\", serif;
            color: var(--texto);
            background:
                radial-gradient(circle at 15% 20%, #fff8e7 0%, transparent 42%),
                radial-gradient(circle at 85% 85%, #fde8d5 0%, transparent 38%),
                var(--fondo);
            padding: 1rem;
        }

        .card {
            width: min(92vw, 680px);
            background: var(--panel);
            border: 1px solid var(--borde);
            border-radius: 18px;
            padding: clamp(1.2rem, 3vw, 2rem);
            box-shadow: 0 18px 40px rgba(31, 41, 55, 0.10);
            text-align: center;
        }

        h1 {
            margin: 0;
            font-size: clamp(1.6rem, 4vw, 2.4rem);
            font-weight: 600;
            letter-spacing: 0.02em;
        }

        p {
            margin: 0.9rem 0 0;
            font-size: clamp(1rem, 2.2vw, 1.1rem);
            line-height: 1.6;
            color: #3f4754;
        }

        .firma {
            margin-top: 1.2rem;
            display: inline-block;
            font-size: 0.93rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--detalle);
            border-top: 1px solid var(--borde);
            padding-top: 0.75rem;
        }
    </style>
</head>
<body>
    <main class=\"card\">
        <h1>Bienvenido al servidor simulado</h1>
        <p>Conexion estable y respuesta activa.</p>
        <span class=\"firma\">Hecho por Saimol Jimenez</span>
    </main>
</body>
</html>"""

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=UTF-8\r\n"
        f"Content-Length: {len(body.encode('utf-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )

    conexion.sendall(response.encode("utf-8"))
    conexion.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor simulado escuchando en {HOST}:{PORT}")

while True:
    conexion, direccion = server.accept()
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
    hilo_cliente.start()