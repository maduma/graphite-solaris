import chunker.separatorline_map
import socket
import re
from .. import config

prefix = '{0}.{1}.{2}'.format(
    config.LABEL, socket.gethostname(), config.DLSTAT)

# dlstat data are normalised (bytes/s)
def transform(chunk):
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
    pattern = re.compile('^\d{10}$')
    return chunker.separatorline_map.get_iterator(
        stream.lines, pattern, transform)
