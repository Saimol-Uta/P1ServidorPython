from multiprocessing import Process, Pipe

def enviar(conn):
    conn.send("Hola desde el proceso hijo!")
    conn.close()

def recibir(conn):
    mensaje = conn.recv()
    print("Mensaje recibido en el proceso padre:", mensaje)
    conn.close()

if __name__ == "__main__":

    conn1, conn2 = Pipe()
    p1 = Process(target=enviar, args=(conn1,))
    p2 = Process(target=recibir, args=(conn2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()