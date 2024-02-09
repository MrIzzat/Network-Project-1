import time
from socket import *

sn = "192.168.1.255"
port = 5566
c = 0
clsoc = socket(AF_INET,SOCK_DGRAM)
x = "Jihad"
while True:
    clsoc.sendto(x.encode(),(sn,port))
    print(x)
    time.sleep(5)
clsoc.close()