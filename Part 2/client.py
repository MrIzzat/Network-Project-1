import time
from socket import *

# Load the IP in the sn variable, This is the broadcast IP for my router, can be different depending on router
sn = "192.168.1.255"
# Load port into the port variable
port = 5566
# Create a UDP socket in th AF_INET IPv4 family into the clsoc variable
clsoc = socket(AF_INET,SOCK_DGRAM)
# Loading the name into the x variable
x = "Izzat Almustafa"
# Begin message sending process to the broadcast IP
while True:
    # Send the message (encoded)  to the IP using the previously created socket to the IP and port previously defined.
    clsoc.sendto(x.encode(),(sn,port))
    print(x)
    # Delay the message sending by 2 seconds.
    time.sleep(2)
clsoc.close()