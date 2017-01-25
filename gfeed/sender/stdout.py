from .. import config

print(dir())

def get_iterator(it):
    for line in it:
        if line != config.HINT:
            print(line)
            yield
