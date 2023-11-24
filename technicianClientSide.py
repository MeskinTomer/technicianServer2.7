"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging
from protocol import *
from client_functions import *

logging.basicConfig(filename='technicianClient_log.log', level=logging.DEBUG)


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
    except socket.error as err:
        logging.error('Received socket error ' + str(err))
        logging.debug('The client socket has been closed')


if __name__ == '__main__':
    main()
