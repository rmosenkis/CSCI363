import select
import socket
import sys

# Function to broadcast messages to all connected clients
def broadcast_data(sock, message, nickname):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(nickname + ": " + message.encode())
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

# Function to handle client quit command
def handle_client_quit(sock):
    sock.close()
    CONNECTION_LIST.remove(sock)

if __name__ == "__main__":
    # Get port number from command line
    if len(sys.argv) != 2:
        print("Usage: chat_server <port>")
        sys.exit()
    PORT = int(sys.argv[1])

    # Set maximum number of clients to 100
    MAX_CLIENTS = 100

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(MAX_CLIENTS)

    # Add server socket to the list of readable connections
    CONNECTION_LIST = [server_socket]

    print("Chat server started on port " + str(PORT))

    nickname = "User"

    while True:
        # Get the list of sockets that are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            
            # New connection
            if sock == server_socket:
                sockfd, client_address = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) connected" % client_address)
                broadcast_data(sockfd, "[%s:%s] entered the chat\n" % client_address, nickname)
            # Incoming message from a client
            else:
                data = sock.recv(4096).decode()
                if data:
                    # Handle client nickname command
                    if data.startswith("/nick"):
                        nickname = data.split()[1]
                    # Handle client quit command
                    elif data.startswith("/quit"):
                        broadcast_data(sock, "Client (%s, %s) is offline\n" % client_address, nickname)
                        print(nickname + " is offline")
                        handle_client_quit(sock)
                    elif data.startswith("/list"):
                        print(CONNECTION_LIST)
                    else:
                        broadcast_data(sock, data, nickname)
                        print(nickname + ": " + data)
