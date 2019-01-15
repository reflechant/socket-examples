"""
This is a simple console chat over UDP. You need to know your peer IP address to chat
"""
import sys
import socket
import threading

peer_addr = '192.168.1.10'  # your peer's IP
port = 22000


def get_host():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.connect(('10.255.255.255', 80))
        return s.getsockname()[0]

def send(sock):
    while True:
        msg = sys.stdin.readline()
        sock.sendto(msg.encode(), 0, (peer_addr, port))

def recv(sock):
    while True:
        data, sender_addr = sock.recvfrom(4096)
        sys.stdout.write("\n", sender_addr[0]+":", data.decode())
        sys.stdout.flush()

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((get_host(), port))

threading.Thread(target=send, args=(sock,)).start()
threading.Thread(target=recv, args=(sock,)).start()