import socket

def handle_client(client : socket.socket):
    # Receives client request 
    req = client.recv(1024)
    print("Request from client",req)

    # Send response with size and corelation_id
    size = 0
    corelation_id = 7
    client.send(size.to_bytes(4, byteorder = "big", signed = True))
    client.send(corelation_id.to_bytes(4, byteorder = "big", signed = True))
    client.close()


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    while True:
        client, _ = server.accept() # wait for client
        handle_client(client)



if __name__ == "__main__":
    main()
