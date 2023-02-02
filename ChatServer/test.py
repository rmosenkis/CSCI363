import socket
import threading

nicknames = []
clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!", client)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of client is {nickname}!")
        broadcast(f"{nickname} joined the chat!", client)
        client.send("Connected to the server!".encode("utf-8"))
        client.recv(1024).decode("utf-8")
        handle_thread = threading.Thread(target=handle, args=(client,))
        handle_thread.start()

def main(port):
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(100)
    print("Server started!")
    receive()

if __name__ == "__main__":
    main(8890)