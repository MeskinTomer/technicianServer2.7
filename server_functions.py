"""
Author: Tomer Meskin
Date: 24/11/2023
Description:
"""
import base64
import logging
import glob
import os
import shutil
import subprocess
from PIL import ImageGrab

logging.basicConfig(filename='server_functions_log.log', level=logging.DEBUG)


def dir_file(file):
    try:
        my_file = file + '/*.*'
        file_dir = glob.glob(my_file)
        file_dir = ', '.join(file_dir).replace('\\', '/')
        print(file_dir)
        logging.debug('Dir command was executed successfully')
    except FileNotFoundError:
        file_dir = 'Error'
        logging.error('Dir command has crashed')
    return file_dir


def del_file(file):
    success = 'File was Deleted successfully'
    try:
        os.remove(file)
        logging.debug('Del command was executed successfully')
    except FileNotFoundError:
        success = 'Error'
        logging.error('Del command has crashed')
    return success


def copy_file(source_file, destination_file):
    success = 'File was copied successfully'
    try:
        shutil.copy(source_file, destination_file)
        logging.debug('Copy command was executed successfully')
    except shutil.Error:
        success = 'Error'
        logging.error('Copy command has crashed')
    return success


def open_program(program_path):
    success = 'Program was executed successfully'
    try:
        subprocess.call(program_path)
        logging.debug('Open command was executed successfully')
    except OSError as err:
        success = 'Error'
        logging.error('Open command has crashed')
    except subprocess.CalledProcessError as err:
        success = 'Error'
        logging.error('Open command has crashed')
    return success


def take_screenshot():
    try:
        ImageGrab.grab(all_screens=True).save('screenshot.jpg')
        with open('screenshot.jpg', 'rb') as img:
            ret_val = base64.b64encode(img.read()).decode('utf-8')
        os.remove('screenshot.jpg')
        logging.debug('Screenshot command was executed successfully')
    except OSError as err:
        ret_val = ''
        logging.error('Screenshot command has crashed', err)
    return ret_val
