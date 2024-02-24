import socket
from _thread import *

server = "192.168.2.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


pos = [50, 50]


def threaded_client(conn, player):
    conn.send(str.encode(str(pos[player])))
    reply = ""
    while True:
        try:
            data = int(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received:", data)
                print("Sending:", reply)

            conn.sendall(str.encode(str(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


current_player = 0
while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection, current_player))
    current_player += 1
