import socket
import threading
import time

server_ip = '127.0.0.1'
server_port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server_ip, server_port))

s.listen()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, conn, addr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.addr = addr
        self.conn = conn

    def run(self):
        print(f"Starting threadname: {self.name}, ThreadID: {self.threadID}")
        print('connected by', self.addr)
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            self.conn.sendall(data)

            msg = data.decode("utf_8")
        self.conn.close()
        print(msg)

connectionID = 0

while True:
    conn, addr = s.accept()
    x = myThread(connectionID, "Thread-1", 1, conn, addr)
    connectionID += 1
    x.start()

