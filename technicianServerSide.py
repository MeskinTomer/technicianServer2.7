"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging
from server_functions import *
from protocol import *
logging.basicConfig(filename='technicianServer_log.log', level=logging.DEBUG)

QUEUE_LEN = 1


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = server_socket.accept()
            logging.debug('A client has connected to the server || address: ' + ''.join(map(str, client_address)))
            try:
                while True:
                    request = protocol_recv(client_socket)
                    com = request[0]
                    payload = request[1]
                    logging.debug('The command ' + com + ' has been received')
                    print('Received the command: ' + com)
                    response = ''
                    if com == 'DIR':
                        response = dir_file(payload)
                    elif com == 'DELETE':
                        del_file(payload)
                    elif com == 'COPY':
                        path1 = payload.split('|')[0]
                        path2 = payload.split('|')[1]
                        response = copy_file(path1, path2)
                    elif com == 'EXECUTE':
                        response = open_program(payload)
                    elif com == 'TAKE_SCREENSHOT':
                        response = take_screenshot()
                    elif com == 'EXIT':
                        client_socket.send(protocol_send('You were disconnected', ''))
                        break
                    else:
                        response = 'Invalid command'
                    client_socket.send(protocol_send(com, response))
                    logging.debug('The message ' + com + ' + ' + response + ' has been sent')
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
                logging.debug('The client has been disconnected')
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        server_socket.close()
    open_program('C:/Windows/System32/notepad.exe')


if __name__ == '__main__':
    main()
