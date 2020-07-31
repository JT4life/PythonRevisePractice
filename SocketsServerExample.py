import socket
#Socket are endpoints that receives data, you send and receive data
#1234 is our port number example
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1200))
s.listen(5)
#if anyone connects, clientsocket is just our obj
while True:
    clientsocket, address = s.accept()
    print('Connection from',address, 'has been established!')
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    # send info to client socket