import buffer.hint
import socket

SERVER='graphitea.svr.luxair'
PORT=2003

def send_tcp(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER, PORT))
    s.sendall(msg)
    s.close()
    print(msg),

def get_iterator(formater_it):
    buffer_it = buffer.hint.get_buffer(formater_it)
    for buf in buffer_it:
        print(buf)
        buf.append('\n')
        send_tcp('\n'.join(buf))
        yield
