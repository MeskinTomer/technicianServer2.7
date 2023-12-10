"""
Author: Tomer Meskin
Date: 24/11/2023
Description:
"""

import socket
import logging


def protocol_send(cmd, msg):
    cmd_len = len(cmd)
    msg_len = len(msg)
    total_message = str(cmd_len).encode() + '!'.encode() + cmd.encode() + str(msg_len).encode() + '!'.encode() + msg.encode()
    return total_message


def protocol_recv(my_socket):
    cur_char = ''
    cmd_len = ''
    msg_len = ''
    try:
        while cur_char != '!':
            cur_char = my_socket.recv(1).decode()
            cmd_len += cur_char
        cmd_len = cmd_len[:-1]

        cmd = my_socket.recv(int(cmd_len)).decode()

        cur_char = ''

        while cur_char != '!':
            cur_char = my_socket.recv(1).decode()
            msg_len += cur_char
        msg_len = msg_len[:-1]

        msg = my_socket.recv(int(msg_len)).decode()

        final_message = (cmd, msg)
    except socket.error:
        final_message = ('Error', '')
    return final_message

