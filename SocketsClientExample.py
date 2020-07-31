import socket
#Socket are endpoints that receives data, you send and receive data

#this is a stream of data bytes
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1200))
#how many chunks of data to receive at a time, in this case 1024
msg = s.recv(1024)
print(msg.decode("utf-8"))
#decode the bytes