import chunker.dlstat


def tranform(chunk, period):
    epoch = chunk.pop(0).rstrip()
    for line in chunk:
        (zone, interface, rbytes, obytes) = line.rstrip().split(':')
        interface = interface.split('/')[-1] # remove zone in interface name
        rbytes = int(int(rbytes) / period) # normalisation bytes/sec
        obytes = int(int(obytes) / period)
        total_bytes = str(rbytes + obytes) # add a new stat
        msg = '{0}.{1}.{{0}} {{1}} {2}\n'.format(zone, interface, epoch)
        yield msg.format('bytes', total_bytes)
        yield msg.format('rbytes', rbytes)
        yield msg.format('obytes', obytes)

def get_iterator(stream):

    it = chunker.dlstat.get_iterator(stream.it)
    period = stream.period

    def iterator():
        for chunk in it:
            print "-----------------------------"
            for line in tranform(chunk, period):
                yield line
    
    return iterator()
