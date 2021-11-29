import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

host = socket.gethostname()		
port = int(sys.argv[1])			        

msg = "PING"

sock.settimeout(1)
for i in range(10):
    sock.sendto(msg.encode(),(host,port))

    try:
        data, addr = sock.recvfrom(1024)
        print(f"{i+1} : sent {msg}... recieved {data.decode()}")
    except:
        print(f"{i+1} : sent {msg}... Timed Out")

sock.close()

