"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import logging
import base64
import binascii
from protocol import *
from PIL import Image
from io import BytesIO

logging.basicConfig(filename='technicianClient_log.log', level=logging.DEBUG)

COMMANDS = ['DIR', 'DELETE', 'COPY', 'EXECUTE', 'TAKE_SCREENSHOT', 'EXIT']


def command(com):
    """
    validates the command from the user
    :param com: The command entered by the user
    :type: string
    :return: either the validated command or either "Invalid" for invalid commands
    """
    if com not in COMMANDS:
        com = 'Invalid'
    return com


def reshape_file_path(path):
    """
    forms the file path, so it could be sent to the server
    :param path: The path needed to be shaped
    :type: string
    :return: the path reshaped
    """
    return path.replace('\\', '/')


def save_image(image_str):
    """
    saves an image to the folder
    :param image_str: The string containing the image
    :type: string
    :return: None
    """
    try:
        decoded_image = base64.b64decode(image_str)

        image = Image.open(BytesIO(decoded_image))
        image.save('received_image.jpg', 'jpeg')
        image.show()
    except binascii.Error:
        logging.error('Error while trying to decode image')
        print('Error decoding image')


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
        print("Available commands are:\n" + ', '.join(COMMANDS))
        while True:
            com = input("Enter the desired command")
            com = command(com)
            if com == 'COPY':
                first_path = reshape_file_path(input('Enter the source path'))
                second_path = reshape_file_path(input('Enter the destination path'))
                payload = first_path + '|' + second_path
            elif com == 'TAKE_SCREENSHOT' or com == 'EXIT':
                payload = ''
            else:
                payload = input('Enter file path')

            if com != 'Invalid':
                my_socket.send(protocol_send(com, payload))
                logging.debug('The command ' + com + ' has been sent to the server')
                response = protocol_recv(my_socket)
                if response[0] != 'TAKE_SCREENSHOT' and response[0] != 'DIR':
                    print('Received the command: ' + response[0] + ' and the response: ' + response[1])
                    logging.debug('Received the command: ' + response[0] + ' and the response: ' + response[1])
                elif response[0] == 'DIR':
                    print('Received the command: ' + response[0] + ' and the response:')
                    li = response[1].split(", ")
                    for file in li:
                        logging.debug(file)
                        print(file)
                else:
                    print('Received the command: ' + response[0])
                    logging.debug('Received the command: ' + response[0])
                    logging.debug('Attempting to save received image')
                    save_image(response[1])
                if response[0] == 'You were disconnected':
                    logging.debug('The server has disconnected the client')
                    break
            else:
                logging.debug('Invalid command has attempted to be sent')
                print('Invalid command')
    except socket.error as err:
        logging.error('Received socket error ' + str(err))
        logging.debug('The client socket has been closed')


if __name__ == '__main__':
    main()
