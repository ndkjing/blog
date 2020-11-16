"""
tcp连接接收数据
"""
# TCPclient.py

import socket


class TcpClient:

    def __init__(self):

        self.target_host = "116.62.44.118"  # 服务器端地址
        self.target_port = 3389  # 必须与服务器的端口号一致

    def start(self):
        while True:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect((self.target_host,self.target_port))
            data = input(">")
            if not data:
                break
            client.send(data.encode())
            response = client.recv(1024)
            print(response)
        client.close()


if __name__ == '__main__':
    obj = TcpClient()
    obj.start()
#
#
# import socket
# import threading
# client_list = []
# def read_server(client_socket):
#     while True:
#         content = client_socket.recv(2048).decode('UTF-8')
#         if content is not None:
#             print("content:",content)
#
# client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ## 绑定USR-K7 开启的IP地址和端口号
# client_socket.connect(('192.168.0.7',23))
# threading.Thread(target=read_server,args=(client_socket,)).start()
# while True:
#     line = input('')
#     if line is None or line =='exit':
#         break
#     client_socket.send(line.encode("UTF-8"))







