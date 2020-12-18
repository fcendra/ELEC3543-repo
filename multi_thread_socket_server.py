#!/usr/bin/env python3
# filename : multi_thread_socket_server.py
# This prog. - adapted from Python Netw. Prog. Cookbook - 
# is optimized for Python 3.6 or above
# It may run on any other Python with/without modification

import os
import socket
import threading
import socketserver

# Sample Prog. 13 - A multi-threaded server prog.
server_host = 'localhost'
server_port = 0
buff_sz = 2048

# define the client module
def client(ip, port, msg):
    # A client to test the multi-threaded (ThreadingMixIn class) server 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    try:
        s.sendall(msg.encode())
        response = s.recv(buff_sz)
        print("Client received: ", response.decode())
    finally:
        s.close()

# define a class for each threaded TCP request handler
class ThreadTCPRqxHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s"%(current_thread.name, data.decode())
        self.request.sendall(response.encode())


# define a class for multi-threaded TCP server
class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # nothing to add here, inherited everything from the parent classes
    pass

if __name__ == '__main__':
    # Run the server
    server = ThreadTCPServer((server_host, server_port), ThreadTCPRqxHandler)
    ip, port = server.server_address # retrieve the ip address
    # Start a thread with the server -- 1 thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running on thread: ", server_thread.name)
    # Run multiple clients
    client(ip, port, "Greeting msg from client #1")
    client(ip, port, "Greeting msg from client #2")
    client(ip, port, "Greeting msg from client #3")
    # server cleanup
    server.shutdown()


# Expected output :
# > python3 multi_thread_socket_server.py
# Server loop running on thread:  Thread-1
# Client received:  Thread-2: Greeting msg from client #1
# Client received:  Thread-3: Greeting msg from client #2
# Client received:  Thread-4: Greeting msg from client #3
#

