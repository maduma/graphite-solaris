# dlstat reader iterator
import cmdreader
from .. import config

def get_stream(period):

    cmd = '/usr/sbin/dlstat -p -o zone,link,rbytes,obytes -T u'.split()
    cmd.append(str(period))

    return cmdreader.get_stream(cmd, period, name=config.DLSTAT)
