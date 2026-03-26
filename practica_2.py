from multiprocessing import Process, queues
import time

def productor(q):
    for i in range(5):
        mensaje = f"Mensaje {i}"
        q.put(mensaje)
        time.sleep(1)

def consumidor(q):
    mensaje = q.get()
    print("Mensaje recibido en el consumidor:", mensaje)

if __name__ == "__main__":
    q = queues.Queue()
    p1 = Process(target=productor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()