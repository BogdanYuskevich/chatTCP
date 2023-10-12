import socket
import time

# Налаштовуємо адресу та порт для сервера
HOST = '127.0.0.1'  # Адреса сервера (в даному випадку - localhost)
PORT = 12345  # Порт сервера

# Створюємо сокет сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Прослуховуємо порт
server_socket.listen(1)

print(f"Сервер слухає на {HOST}:{PORT}...")

# Очікуємо підключення клієнта
client_socket, client_address = server_socket.accept()
print(f"Підключено клієнта з адресою {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] Отримано: {data.decode('utf-8')}")

    # Перевірка, чи отримано команду для закриття з'єднання
    if data.decode('utf-8') == 'exit':
        break

# Закриваємо з'єднання
client_socket.close()
server_socket.close()
