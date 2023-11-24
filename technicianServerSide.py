"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging
from protocol import *
from server_functions import *

logging.basicConfig(filename='technicianServer_log.log', level=logging.DEBUG)

QUEUE_LEN = 1


def main():


    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try:
    #     server_socket.bind(('0.0.0.0', 1729))
    #     server_socket.listen(QUEUE_LEN)
    #     while True:
    #         client_socket, client_address = server_socket.accept()
    #         logging.debug('A client has connected to the server || address: ' + ''.join(map(str, client_address)))
    # except socket.error as err:
    #     print('received socket error on server socket' + str(err))
    # finally:
    #     server_socket.close()


if __name__ == '__main__':
    main()
