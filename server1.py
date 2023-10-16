import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
while True:
    print("Server listening at {}:{}".format(server_address[0], server_address[1]))
    print("CONNECT ALREADY")
    client_socket, client_address = server_socket.accept()
    print("Connected with client {}".format(client_address))
    while True:
        received_data = client_socket.recv(1024) 
        
        received_text = received_data.decode('utf-8')
        expected_size = client_socket.recv(1024).decode('utf-8')
        if received_text.lower() == "exit":
            print("Connection terminated by user.")
            break
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("Client says: {}".format(received_text))
        print("at time: {}".format(current_time))
        
        response = "Server received your message: '{}'".format(received_text)
        if int(len(received_text)) == int(expected_size):
            print("String length is consistent.")
        else:
            print("String length is INCONSISTENT: stated {}, received {}".format(expected_size, len(received_text)))
            response += ", but data was lost in transmission."
        client_socket.send(response.encode('utf-8'))
        
    client_socket.close()

server_socket.close()