# file reader iterator
def get_stream(path):

    # read period value
    def period():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('# period:'):
                    return int(line.split(':')[1])
        raise LookupError('Cannot found period in file')

    def iterator():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('#'): continue
                yield line
    
    class Stream:
        def __init__(self):
            self.period = period()
            self.it = iterator()
        def close(self):
            pass

    return Stream()
