from socket import *
import time

# Set up the port
port = 5566
# Set up the Socket
svsoc = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the port
svsoc.bind(("", port))
print("Server is Ready")
print("_________________________________________________________________")
# Setting up the names, IPs and Times lists
lsName = []
lsIP = []
lsTime = []
# flag
ch = 0

# Begin the message receiving proccess
while (True):
    # Receive information from the broadcast IP
    msg, CliAdr = svsoc.recvfrom(2048)
    # Store the IP from the CliAdr tuple's first index
    ip = CliAdr[0]
    # Decode the message
    msg = msg.decode()
    # Run a for loop to see if the message's sender has sent a message previously
    # By checking the if the IP is in the IP list
    for i in range(len(lsName)):
        # If IP is found, update the last message's time
        if (ip == lsIP[i]):
            t2 = time.ctime(time.time())
            lsTime[i] = t2
            ch = 1
    # If IP not found in IP list, add it along with the IP and the new time into the lists
    if (ch == 0):
        lsName.append(msg)
        t2 = time.ctime(time.time())
        lsTime.append(t2)
        lsIP.append(ip)
    # Print the list of clients names and their times
    for i in range(len(lsIP)):
        print("Message from " + lsName[i] + " at", lsTime[i])
    print("_________________________________________________________________")
    # Reset flag
    ch = 0
    # If a client sends x, the server will close
    if ("x" in msg):
        break

print("end")
