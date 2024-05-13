import socket
import hashlib

# Encryption and Decryption Functions
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) + key)
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr(ord(char) - key)
        decrypted_message += decrypted_char
    return decrypted_message

# Server Code
def server_program():
    # Create a socket object
    server_socket = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # Bind to the port
    server_socket.bind(('', port))

    # Wait for client connection
    server_socket.listen(5)

    print("Server is listening...")

    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print("Got connection from", addr)

    # Set the encryption key
    key = 5

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        print("Received message:", message)

        # Decrypt the message
        decrypted_message = decrypt_message(message, key)
        print("Decrypted message:", decrypted_message)

        # Send response back to client
        response = input("Enter response: ")
        encrypted_response = encrypt_message(response, key)
        client_socket.send(encrypted_response.encode())

    # Close the connection
    client_socket.close()

# Client Code
def client_program():
    # Create a socket object
    client_socket = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # Connect to the server
    client_socket.connect(('localhost', port))

    # Set the encryption key
    key = 5

    while True:
        # Send message to server
        message = input("Enter message: ")
        encrypted_message = encrypt_message(message, key)
        client_socket.send(encrypted_message.encode())

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print("Received response:", response)

        # Decrypt the response
        decrypted_response = decrypt_message(response, key)
        print("Decrypted response:", decrypted_response)

    # Close the connection
    client_socket.close()

# Run the server or client program
if __name__ == "__main__":
    print("Do you want to run the server or client?")
    print("1. Server")
    print("2. Client")
    choice = input("Enter your choice: ")

    if choice == "1":
        server_program()
    elif choice == "2":
        client_program()
    else:
        print("Invalid choice")