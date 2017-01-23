# iostat reader iterator
import cmdreader

def stream(period):

    cmd = ['/usr/bin/iostat', '-xnz', str(period)]
    st = cmdreader.stream(cmd, period)
    return st
