import socket
import threading

# Налаштовуємо адресу та порт сервера
HOST = '127.0.0.1'  # Адреса сервера (в даному випадку - localhost)
PORT = 12345  # Порт сервера

# Список для збереження підключених клієнтів
clients = []

# Створюємо сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            # Відправляємо отримане повідомлення всім підключеним клієнтам
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        # Якщо не вдалося відправити повідомлення, видаляємо клієнта зі списку
                        clients.remove(client)
        except:
            # Якщо сталася помилка, видаляємо клієнта зі списку
            clients.remove(client_socket)
    client_socket.close()

while True:
    # Очікуємо підключення нового клієнта
    client_socket, client_address = server_socket.accept()
    print(f"Підключено клієнта з адресою {client_address}")

    # Додаємо клієнта до списку
    clients.append(client_socket)

    # Запускаємо окремий потік для обробки клієнта
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
