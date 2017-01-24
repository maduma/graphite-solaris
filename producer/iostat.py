# iostat reader iterator
import cmdreader

def get_stream(period):
    
    cmd = ['/usr/bin/iostat', '-xnz', str(period)]
    return cmdreader.get_stream(cmd, period)
