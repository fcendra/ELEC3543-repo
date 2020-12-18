#!/usr/bin/env python3
# filename : echo_server.py
# This prog. - adapted from Python Netw. Prog. Cookbook - 
# is optimized for Python 3.6 or above
# It may run on any other Python with/without modification

import socket
import sys
import argparse

host = 'localhost'
data_buff_sz = 2048
backlog = 5    # the max. no of queued connections

def echo_server(port):
    # Samp. Prog. 12B - a more complete echo server using input arguments
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_addr = (host, port)
    print("Starting up echo server on ", server_addr)
    s.bind(server_addr)
    # Listen to the clients, with the backlog specifying the max no of que.conns
    s.listen(backlog)
    while True:
        print("Waiting to receive message from client")
        client, address = s.accept()
        data = client.recv(data_buff_sz)
        if data:
            print("Data : ", repr(data))
            client.send(data)   # echo/send back the data being received      
            print("sent ", len(data), " bytes to ", address)
        # close/terminate the connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


# Expected output :
# > python3 echo_server.py --port=9900
# Starting up echo server on  ('localhost', 9900)
# Waiting to receive message from client
# Data :  b'Roger, testing message. This will be echoed'
# sent  43  bytes to  ('127.0.0.1', 49550)
# Waiting to receive message from client
#

