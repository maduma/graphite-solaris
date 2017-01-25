import chunker.timestamp
import socket
from .. import config

prefix = '{0}.{1}.{2}'.format(
    config.LABEL, socket.gethostname(), config.DLSTAT)

# dlstat data are normalised (bytes/s)
def tranform(chunk):
    epoch = chunk.pop(0).rstrip()

    for line in chunk:
        if line.startswith('extended'): continue
        if line.startswith('r/s'): continue
        '''
        (zone, interface, rbytes, obytes) = line.rstrip().split(':')
        total_bytes = str(int(rbytes) + int(obytes)) # add a new stat
        msg = '{0}.{1}.{2}.{{0}} {{1}} {3}'.format(
            prefix, zone, interface, epoch)

        yield msg.format('bytes', total_bytes)
        yield msg.format('rbytes', rbytes)
        yield msg.format('obytes', obytes)
        '''
        yield line.rstrip()

    yield config.HINT # usefull hint for consumer

def get_iterator(stream):

    it = chunker.timestamp.get_iterator(stream.it, discard_first=True)

    def iterator():
        for chunk in it:
            for line in tranform(chunk):
                yield line
    
    return iterator()
