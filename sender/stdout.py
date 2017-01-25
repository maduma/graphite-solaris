def get_iterator(it):
    for line in it:
        if line != 'CHUNK':
            print(line)
            yield
