To Compile and Run the server: "python3 chat_server.py [Port]", where [Port] is the Port number that you choose to connect to.

To connect as a client: "nc [IP Address] [Port], where [IP Address] is the IP Address of the computer on which the server is running and Port is the same Port number that you chose for the server.

This program has four main pieces of functionality. You can send regular messages on the client, which will be received and printed by the server. There are three commands that can be used as well. "/nick" changes the clients nickname to whatever follows the command. This changes the name that is displayed before each message on the server. "/list" will print out all currently connected clients to the server. "/quit" will disconnect the client from the server.
