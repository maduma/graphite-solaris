# file reader iterator
def stream(path):

    # read period value
    def get_period():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('# period:'):
                    return int(line.split(':')[1])

    def iterator():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('#'): continue
                yield line
    
    class Stream:
        def __init__(self):
            self.period = get_period()
            self.it = iterator()
        def close(self):
            pass

    return Stream()
