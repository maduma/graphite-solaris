import chunker.separatorline_map
import socket
import re
from .. import config

prefix = '{0}.{1}.{2}'.format(
    config.LABEL, socket.gethostname(), config.ZONESTAT)

# kilobytes to bytes
def kb2b(value):
    if value.endswith('K'):
        return str(int(value[:-1]) * 1024)
    return value

def transform(chunk):
    epoch = chunk.pop(0).rstrip().split(':')[-3]

    for line in chunk:
        if 'footer' in line: continue
        if '[resource]' in line:
            (cpu, mem, vmem) = [ kb2b(x) for x in line.rstrip().split(':')[4:7] ]
            msg = '{0}.max.{{0}} {{1}} {1}'.format(prefix, epoch)
            yield msg.format('cpu', cpu)
            yield msg.format('mem', mem)
            yield msg.format('vmem', vmem)
            continue

        fields = [ kb2b(x.rstrip('%')) for x in line.split(':')[3:13] ]
        (zone, cpu, cpup, _, _, mem, memp, _, vmem, vmemp) = fields
        zone = zone.lstrip('[').rstrip(']')
        if zone not in ['total']: zone = 'zone.' + zone

        msg = '{0}.{1}.{{0}} {{1}} {2}'.format(prefix, zone, epoch)

        yield msg.format('cpu', cpu)
        yield msg.format('cpup', cpup)
        yield msg.format('mem', mem)
        yield msg.format('memp', memp)
        yield msg.format('vmem', vmem)
        yield msg.format('vmemp', vmemp)

    yield config.HINT # usefull hint for consumer


def get_iterator(stream):
    pattern = re.compile('\d+:interval:header:since-last-interval:\d+.*')
    it = chunker.separatorline_map.get_iterator(
        stream.it, pattern, transform, discard_first=False)
    return it
