import socket 
import random

# Параметры сервера очереди
HOST = '127.0.0.1'
PORT = 65432

# Список возможных SQL-запросов
queries = [
   "SELECT pg_sleep(1); SELECT * FROM users;",
   "SELECT pg_sleep(1); SELECT name FROM products WHERE price > 100;",
]

# Функция для отправки запроса и получения результата
def send_request(request):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.connect((HOST, PORT))
       s.sendall(request.encode())
       data = s.recv(1024).decode()
       print(f"Результат запроса: {data}")

# Генерирование и отправка запросов
for query in queries:
   print(f"Отправка запроса: {query}")
   send_request(query)