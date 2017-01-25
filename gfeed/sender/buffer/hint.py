from ... import config

def get_buffer(it):
    buf = []
    for line in it:
        if line == config.HINT and buf:
            yield buf
            buf = []
        else:
            buf.append(line)
