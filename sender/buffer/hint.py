def get_buffer(it):
    buf = []
    for line in it:
        if line == 'CHUNK' and buf:
            yield buf
            buf = []
        else:
            buf.append(line)
