
import socket


def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" --> ")  # take input

    while message.strip() != 'q':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(4096).decode()  # receive response

        print('Response from server: ' + data)  

        message = input(" --> ") 

    client_socket.close()  # closes the connection


if __name__ == '__main__':
    client_program()

