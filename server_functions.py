"""
Author: Tomer Meskin
Date: 24/11/2023
Description:
"""

import socket
import logging
import glob
import os
import shutil
import subprocess
import pyautogui


    def dir_file(file):
        try:
            my_file = file + '/*.*'
            file_dir = glob.glob(my_file)
        except FileNotFoundError:
            file_dir = 'Error'
        return file_dir


    def del_file(file):
        success = 'File was Deleted successfully'
        try:
            os.remove(file)
        except FileNotFoundError:
            success = 'Error'
        return success


    def copy_file(source_file, destination_file):
        success = 'File was copied successfully'
        try:
            shutil.copy(source_file, destination_file)
        except shutil.Error:
            success = 'Error'
        return success


    def open_program(program_path):
        success = 'Program was executed successfully'
        try:
            subprocess.call(program_path)
        except FileNotFoundError:
            success = 'Error'
        return success


    def take_screenshot():
        image = pyautogui.screenshot()
        image.save(r'screen.jpg')