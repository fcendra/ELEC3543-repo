#!/usr/bin/env python3
# filename : echo_client.py
# This prog. - adapted from Python Netw. Prog. Cookbook - 
# is optimized for Python 3.6 or above
# It may run on any other Python with/without modification

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    # A more complete echo client using input arguments and try-block
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server thru' a specific port
    server_addr = (host, port)
    print("Connecting to ", server_addr)
    s.connect(server_addr)

    # Using try-block to send data
    try:
        # send data
        msg = "Roger, testing message. This will be echoed"
        print("Sending ", msg)
        s.sendall(msg.encode())
        # wait for response [i.e. the echoed msg] from the server
        msg_len_received = 0
        msg_len_expected = len(msg)
        while (msg_len_received < msg_len_expected):
            data = s.recv(16);
            msg_len_received += len(data)
            print("Received: ", data)
    except socket.errno as e:
        print("Socket error: ", e)
    except Exception as e:
        print("Other exception: ", e)
    finally:
        print("Closing connection to the server !")
        s.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)


# Expected output :
# > python3 echo_client.py --port=9900
# Connecting to  ('localhost', 9900)
# Sending  Roger, testing message. This will be echoed
# Received:  b'Roger, testing m'
# Received:  b'essage. This wil'
# Received:  b'l be echoed'
# Closing connection to the server !
#
# Exceptional case:
# > python3 echo_client.py --port=1900
# Connecting to  ('localhost', 1900)
# Traceback (most recent call last):
#  File "echo_client.py", line 48, in <module>
#    echo_client(port)
#  File "echo_client.py", line 20, in echo_client
#    s.connect(server_addr)
# ConnectionRefusedError: [Errno 61] Connection refused
#
