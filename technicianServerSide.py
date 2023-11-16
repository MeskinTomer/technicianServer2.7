"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging

logging.basicConfig(filename='technicianServer_log.log', level=logging.DEBUG)

QUEUE_LEN = 1


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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = server_socket.accept()
            logging.debug('A client has connected to the server || address: ' + ''.join(map(str, client_address)))
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
