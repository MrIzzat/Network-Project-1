from socket import *

import os.path


# not found html script that takes the IP address and the client port as arguments
def not_found(IP, clientPort):
    website = ''''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
           <link rel="stylesheet" type="text/css" href="styles.css">
            <title>Error 404</title>
        </head>
        <body>
              <h1 style="color: red">The file is not found</h1>
              <p style="text-align: left; font-size: 30px;">
                <b>
                  <br>
                  1200704 - Jihad Anfous
                  <br>
                  1200861 - Maryan Qassis
                  <br>
                  1202444 - Izzat Ibrahim
                </b>
                <br>
                <br>
                IP Address: ''' + str(IP) + '''
                <br>
                Client Port: ''' + str(clientPort) + '''

              </p>

        </body>
        </html>
        '''''
    return website


def display_not_found(website, IP, port):
    connection.send("HTTP/1.1 404 Not Found \r\n".encode())
    connection.send("Content-type: text/html \r\n".encode())
    connection.send("\r\n".encode())
    website = not_found(IP, port).encode()
    connection.send(website)


# server port that the clients will connect to
Serverport = 9977
# make a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Associates the socket with its local address, allowing clients to connect to the server using that address.
serverSocket.bind(("", Serverport))
# the server is ready to recieve connections
serverSocket.listen(1)
print("The server is ready to recieve connections.")

while True:
    # accept is called by the server to complete the connection
    connection, address = serverSocket.accept()
    # recieve data from the server and decode it
    get = connection.recv(1024).decode()
    print(address)
    print(get)
    IP = address[0]
    port = address[1]
    # to get the request
    request = get.split(" ")[1]
    request = request.lower()
    request = request.lstrip("/")
    request = request.strip("?")
    print(request)
    # and see if it's one from the following
    if request == "" or request == "index.html" or request == "main_en.html" or request == "en":
        # open english html file
        neededFile = open("main_en.html")
        # read the file
        website = neededFile.read()
        # close the file after reading
        neededFile.close()
        # send an encoded response to the client that the file is found
        connection.send("HTTP/1.1 200 OK\r\n".encode())
        # send file content type
        connection.send("Content-Type: text/html \r\n".encode())
        # send the end of the server response
        connection.send("\r\n".encode())
        # send the encoded html file
        connection.send(website.encode())

    # if the request was ar or main_ar.html
    elif request == "ar" or request == "main_ar.html":
        with open('main_ar.html', 'r', encoding='utf-8') as file:
            website = file.read()

        connection.send("HTTP/1.1 200 OK\r\n".encode())
        connection.send("Content-Type: text/html ;charest=utf-8\r\n".encode())
        connection.send("\r\n".encode())
        connection.send(website.encode())

    # if the request ended with .html
    elif request.endswith(".html"):
        neededFile = open("test.html")
        website = neededFile.read()
        neededFile.close()
        connection.send("HTTP/1.1 200 OK\r\n".encode())
        connection.send("Content-type: text/html \r\n".encode())
        connection.send("\r\n".encode())
        connection.send(website.encode())

    # if the request ended with .css
    elif request.endswith(".css"):
        neededFile = open("styles.css", "r")
        website = neededFile.read()
        neededFile.close()
        connection.send("HTTP/1.1 200 OK\r\n".encode())
        connection.send("Content-type: text/css \r\n".encode())
        connection.send("\r\n".encode())
        connection.send(website.encode())

    # if the request ended with .png
    elif request.endswith(".png"):
        # if file exists
        if os.path.exists(request):
            neededFile = open(request, "rb")
            website = neededFile.read()
            neededFile.close()
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send("Content-type: image/png \r\n".encode())
            connection.send("\r\n".encode())
            connection.send(website)
        else:
            display_not_found(website, IP, port)


    # if the request ended with .jpg
    elif request.endswith(".jpg"):
        if os.path.exists(request):
            neededFile = open(request, "rb")
            website = neededFile.read()
            neededFile.close()
            connection.send("HTTP/1.1 200 OK\r\n".encode())
            connection.send("Content-type: image/jpeg \r\n".encode())
            connection.send("\r\n".encode())
            connection.send(website)
        else:
            display_not_found(website, IP, port)

    # if the request was yt then go to youtube
    elif request == "yt":
        connection.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connection.send("Location: https://www.youtube.com/ \r\n".encode())
        connection.send("\r\n".encode())

    # if the request was so then go to stackoverflow website
    elif request == "so":
        connection.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connection.send("Location: https://stackoverflow.com/ \r\n".encode())
        connection.send("\r\n".encode())

    # if the request was rt then go to ritaj
    elif request == "rt":
        connection.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connection.send("Location: https://ritaj.birzeit.edu/ \r\n".encode())
        connection.send("\r\n".encode())

    # else the request is not found
    else:
        display_not_found(website, IP, port)

    # close the connection after sending the request
    connection.close()