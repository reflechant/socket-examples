"""
This program sends one broadcast UDP packet over local network
"""
import socket
import ipaddress
port = 22000
netmask = '255.255.255.0'

my_addr = socket.gethostbyname(socket.gethostname())

broadcast_addr = '.'.join(my_addr.split('.')[:-1]+['255'])

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    sock.bind((my_addr, port))
    sock.sendto("Hello, world !".encode(), 0, (broadcast_addr, port))
