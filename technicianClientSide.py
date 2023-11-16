"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging

logging.basicConfig(filename='technicianClient_log.log', level=logging.DEBUG)


def protocol_send(message):
    message_len = len(message)
    final_message = str(message_len) + '!' + message
    return final_message


def protocol_receive(my_socket):
    cur_char = ''
    message_len = ''
    while cur_char != '!':
        cur_char = my_socket.recv(1).decode()
        message_len += cur_char
    message_len = message_len[:-1]
    return my_socket.recv(int(message_len)).decode()


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
    except socket.error as err:
        logging.error('Received socket error ' + str(err))
        logging.debug('The client socket has been closed')


if __name__ == '__main__':
    main()
