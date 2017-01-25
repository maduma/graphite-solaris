import buffer.hint

def get_iterator(it):
    buffer_it = buffer.hint.get_buffer(it)
    for buf in buffer_it:
        for line in buf:
            print(line)
            yield
