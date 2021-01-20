import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 網路位址 192.168.0.114
# 電腦乙太網路位址 192.168.56.1 
s.bind(('192.168.56.1', 8888))

print('bind UDP on 8888....')
while(True):
    # 接收資訊
    data, addr = s.recvfrom(1024)
    print(f"Received from {addr[0]}:{addr[1]}")
