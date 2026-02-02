import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 8080))

# Send message
client_socket.send("Hello Server!".encode())

# Receive reply
reply = client_socket.recv(1024).decode()
print("Server replied:", reply)

# Close socket
client_socket.close()