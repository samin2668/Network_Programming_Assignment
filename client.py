import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

HOST = socket.gethostname()		
PORT = int(sys.argv[1])			        
ADDR = (HOST,PORT)

msg = "PING"

print("Samin Yasar - sy0261")

sock.settimeout(.5)
for i in range(10):
    sock.sendto(msg.encode(),ADDR)

    try:
        data, addr = sock.recvfrom(1024)
        print(f"{i+1} : sent {msg}... recieved {data.decode()}")
    except:
        print(f"{i+1} : sent {msg}... Timed Out")

sock.close()