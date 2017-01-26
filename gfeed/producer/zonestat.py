# dlstat reader iterator
import cmdreader
from .. import config

def get_stream(period):

    cmd = '/usr/bin/zonestat -T u -p'.split()
    cmd.append(str(period))

    return cmdreader.get_stream(cmd, period, name=config.ZONESTAT)
