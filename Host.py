import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "Hello"
s.sendto(data.encode("UTF-8"),("192.168.56.1", 8888))
s.close()
