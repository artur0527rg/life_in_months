import json
import ctypes
import os


def rgb_to_tuple(value:str | list):
    if type(value)==str:
        return tuple(json.loads(value))
    return value

def set_wallpaper(path):
    path = os.path.abspath(os.getcwd()) + '\\' + path
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def message_box(title, msg):
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, msg, title, 0)
