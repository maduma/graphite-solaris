import buffer.hint
import socket
from .. import config

def send_tcp(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((config.SERVER, config.PORT))
    s.sendall(msg)
    s.close()

def get_iterator(formater_it):
    buffer_it = buffer.hint.get_buffer(formater_it)
    for buf in buffer_it:
        buf.append('') # last char must be a NEWLINE
        send_tcp('\n'.join(buf))
        yield
