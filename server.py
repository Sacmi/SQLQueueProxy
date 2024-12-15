import psycopg2
from queue import Queue
import socket
import threading

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "pass"

HOST = '127.0.0.1'
PORT = 65432

request_queue = Queue()

def process_request(conn, cursor, request):
   try:
       cursor.execute(request)
       result = cursor.fetchall()
       conn.commit()
       return result
   except Exception as e:
       return f"Error: {e}"

def handle_client(client_socket, address):
   while True:
       request = client_socket.recv(1024).decode()
       if not request:
           break
       request_queue.put((client_socket, request))
   client_socket.close()

def process_queue():
   conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, 
password=DB_PASSWORD)
   cursor = conn.cursor()

   with open("init_db.sql", "r") as f:
       script = f.read()
       cursor.execute(script)
       conn.commit()

   while True:
       client_socket, request = request_queue.get()
       result = process_request(conn, cursor, request)
       # Отправка результата клиенту
       client_socket.sendall(str(result).encode())
       request_queue.task_done()

   conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

threading.Thread(target=process_queue, daemon=True).start()

print(f"Сервер очереди запущен на {HOST}:{PORT}")

while True:
   client_socket, address = server_socket.accept()
   print(f"Новое соединение от {address}")
   threading.Thread(target=handle_client, args=(client_socket, address), daemon=True).start()