# iostat reader iterator
import cmdreader
from .. import config

def get_stream(period):

    cmd = '/usr/bin/iostat -xnrz -Tu'.split()
    cmd.append(str(period))

    return cmdreader.get_stream(cmd, period, name=config.IOSTAT)
