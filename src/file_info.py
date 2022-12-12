import os
'''
file_info.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 11 DEC 22

Get the size and extension of a file
'''

def get_filesize(filepath):
    filesize = os.stat(filepath).st_size
    return filesize

def get_filetype(filepath):
    filetype = os.path.splitext(filepath)[1]
    return filetype