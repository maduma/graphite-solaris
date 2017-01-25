import chunker.dlstat
import socket
from .. import config

prefix = '{0}.{1}.{2}'.format(
    config.LABEL, socket.gethostname(), config.DLSTAT)

# dlstat data are normalised (bytes/s)
def tranform(chunk):
    epoch = chunk.pop(0).rstrip()

    for line in chunk:
        (zone, interface, rbytes, obytes) = line.rstrip().split(':')

        interface = interface.split('/')[-1] # remove zone in interface name
        total_bytes = str(int(rbytes) + int(obytes)) # add a new stat

        msg = '{0}.{1}.{2}.{{0}} {{1}} {3}'.format(
            prefix, zone, interface, epoch)

        yield msg.format('bytes', total_bytes)
        yield msg.format('rbytes', rbytes)
        yield msg.format('obytes', obytes)

    yield config.HINT # usefull hint for consumer

def get_iterator(stream):

    it = chunker.dlstat.get_iterator(stream.it)

    def iterator():
        for chunk in it:
            for line in tranform(chunk):
                yield line
    
    return iterator()
