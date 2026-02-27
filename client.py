import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (replace with the server machine's IP if needed)
client.connect(("localhost", 5000))
print("Connected to server")


while True:
    color = input("What color would you like your 67 to be? : ")
    if not color:
        break
    bgColor = input("What color would you like your background to be? : ")
    if not bgColor:
        break
    client.send(f"{color} {bgColor}".encode())
    response = client.recv(1024).decode()
    print(f"Server says: {response}")

client.close()