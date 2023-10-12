import socket

# Налаштовуємо адресу та порт сервера
HOST = '127.0.0.1'  # Адреса сервера (в даному випадку - localhost)
PORT = 12345  # Порт сервера

# Створюємо сокет клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Підключаємося до сервера
client_socket.connect((HOST, PORT))

while True:
    message = input("Введіть текст для відправки на сервер (або 'exit' для виходу): ")
    if message == 'exit':
        break

    # Відправляємо дані на сервер
    client_socket.sendall(message.encode('utf-8'))

# Закриваємо з'єднання
client_socket.close()
