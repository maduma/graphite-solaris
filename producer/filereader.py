# file reader iterator
def stream(path):

    # read period value
    period = None
    with open(path, 'r') as f:
        for line in f:
            if line.startswith('# period:'):
                period = int(line.split(':')[1])
                break

    def iterator():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('#'): continue
                yield line

    return { 'period': period, 'iterator': iterator() }
