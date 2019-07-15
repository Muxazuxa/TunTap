from pytun import TunTapDevice
import socket

tun = TunTapDevice(name='mytun')
tun.addr = '192.168.13.10'
tun.up()

port = 6333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((tun.addr, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
