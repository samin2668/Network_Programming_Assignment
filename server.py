import socket
import sys
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     

HOST = socket.gethostname()		        
PORT = int(sys.argv[1])			                
ADDR = (HOST,PORT)

sock.bind(ADDR)

print("Samin Yasar - sy0261")
print("[server] : ready to accept data...")
while True:
    data, addr = sock.recvfrom(1024)	        
    print ("[CLIENT] : ",data.decode())
    if random.random() < 0.7:
        sock.sendto("PONG".encode(), addr)
    else:
        print("[server] : packet dropped")