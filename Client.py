import socket

host = '127.0.0.1'
port = 5555


'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    message = "Bye bye MAMA!!!!!"
    msg = message.encode("utf_8")
    s.sendall(msg)
    data = s.recv(1024)

print('Received', repr(data))

'''

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    count = 0
    while True:
        message  = "Count: "
        msg = message.encode("utf_8")
        s.sendall(msg)
        s.sendall(count.to_bytes(1, 'big'))
        data = s.recv(1024)
        print('received', repr(data))