import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and Port
server_socket.bind(("127.0.0.1", 8080))

# Listen for connections
server_socket.listen(1)
print("Server is listening on port 8080...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print("Connected with:", client_address)

# Receive data
data = client_socket.recv(1024).decode()
print("Client says:", data)

# Send reply
client_socket.send("Hello from Server!".encode())

# Close connections
client_socket.close()
server_socket.close()