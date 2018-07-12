#!/usr/bin/env python

import os


def decoding():

    current_dir = os.getcwd() + "/secret message"
    print(current_dir)
    files_list = os.listdir(current_dir)
    print(files_list)
    saved_path = os.getcwd()
    os.chdir(current_dir)
    for file_name in files_list:
        new_name = file_name.translate(None, '0123456789~!@#$%^&*()_+')
        os.rename(file_name, new_name)
        print("Old name - " + file_name)
        print("New name - " + new_name)
    os.chdir(saved_path)


decoding()

