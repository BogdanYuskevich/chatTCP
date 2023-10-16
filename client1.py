import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)
server_socket.connect(server_address)
while True:
    message = input("SPEAK. ") 
    server_socket.send(message.encode('utf-8')) 
    server_socket.send(str(len(message)).encode('utf-8')) 
    if message.lower() == "exit":
        break
    response = server_socket.recv(1024).decode('utf-8')
    print(response)
    
server_socket.close()