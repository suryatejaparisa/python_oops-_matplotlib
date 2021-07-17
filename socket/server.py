import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  
    server_socket.bind((host, port))  # bind host address and port together

    # no of clients that server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        # Accepts data packet less than 4096 bytes
        data = conn.recv(4096).decode()
        if not data:
            break
        print("Data from Client: " + str(data))
        data = input(' --> ')
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    server_program()

