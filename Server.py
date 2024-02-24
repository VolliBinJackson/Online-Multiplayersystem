import sys
import socket
from _thread import *

port = 5555                                         # Standard
server = "localhost"                                # local IPv4 Address (type ipconfig to view your IP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)                                         # accept only 2 client connections
print("Waiting for connection(s)...")


def clientThread(con):
    con.send(str.encode("--- CONNECTED ---"))
    response = ""
    while True:
        try:
            data = con.recv(2048)
            response = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", response)
                print("Sending: ", response)
                print("\n")
            con.sendall(str.encode(response))
        except:
            break

    print("Lost connection")
    con.close()


# Lookout for request continuously
while True:
    con, addr = s.accept()
    print("Successfully connected to: ", addr)

    start_new_thread(clientThread, (con,))

