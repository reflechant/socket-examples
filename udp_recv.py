"""
This program receives UDP packets
"""
import socket
port = 22000


def get_host():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.connect(('10.255.255.255', 80))
        return s.getsockname()[0]


with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    sock.bind((get_host(), port))
    while True:
        data, sender_addr = sock.recvfrom(4096)
        print(sender_addr, data.decode())
