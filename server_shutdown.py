import socket
import json
from config import LOCALHOST_PORT


def main():
    """
    Sends shutdown command to server
    """
    # create an INET, STREAMing socket, this is TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # connect to the server
    sock.connect(("localhost", LOCALHOST_PORT))

    # send a message
    message = {'signal': 'shutdown'}
    sock.sendall(json.dumps(message).encode('utf-8'))
    sock.close()


if __name__ == "__main__":
    main()
