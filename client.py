import socket
import threading
import getpass

def text_to_hex(text):
    return text.encode('utf-8').hex()

def hex_to_text(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            message = hex_to_text(message)
            if message:
                print(f"{message}")
            else:
                break
        except:
            break

# ----- PLEASE CHANGE HOST TO SERVER IP ADDRESS. EXAMPLE: 192.168.0.10

def start_client(host='127.0.0.1', port=5001):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:

        username = getpass.getuser()
        # print(username+' : ')
        message = input("")
        message = username+' : '+message
        if message.lower() == 'exit':
            client_socket.close()
            break
        message = text_to_hex(message)
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
