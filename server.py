import socket
import threading

clients = []

def broadcast(message, _client_socket):
    for client in clients:
        if client != _client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode())
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print(f"Server started on {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
