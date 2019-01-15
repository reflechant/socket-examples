"""
This program receives UDP packets
"""
import socket
import ipaddress
port = 22000

my_addr = socket.gethostbyname(socket.gethostname())

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
    sock.bind((my_addr, port))
    while True:
        data, sender_addr = sock.recvfrom(4096)
        print(sender_addr, data.decode())
