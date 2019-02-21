from socket import socket


def main():
    client = socket()
    # client.connect(('10.7.152.69', 6789))
    client.connect(('127.0.0.1', 12345))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
