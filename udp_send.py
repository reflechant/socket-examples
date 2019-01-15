"""
This program sends one UDP packet over local network
"""
import socket
import ipaddress
peer_addr = '192.168.1.10'
port = 22000


def get_host():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.connect(('10.255.255.255', 80))
        return s.getsockname()[0]


with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    sock.bind((get_host(), port))
    # broadcast_addr = '.'.join(my_addr.split('.')[:-1] + ['255'])
    sock.sendto("Hello, world !".encode(), 0, (peer_addr, port))
