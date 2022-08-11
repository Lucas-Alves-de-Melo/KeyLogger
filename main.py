import pynput
import re

from pynput.keyboard import Listener

def pegar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla )
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', ' ', tecla)
    print(tecla)

with Listener(on_press=pegar) as l:
    l.join()
