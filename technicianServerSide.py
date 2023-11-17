"""
Author: Tomer Meskin
Date: 16/11/2023
Description:
"""

import socket
import logging
import glob
import os
import shutil
import subprocess
import pyautogui

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


def dir_file(file):
    my_file = file + '/*.*'
    file_dir = glob.glob(my_file)
    return file_dir


def del_file(file):
    os.remove(file)


def copy_file(source_file, destination_file):
    shutil.copy(source_file, destination_file)


def open_program(program_path):
    subprocess.call(program_path)


def take_screenshot():
    image = pyautogui.screenshot()
    image.save(r'screen.jpg')


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
    take_screenshot()


if __name__ == '__main__':
    main()
