# iostat reader iterator
import cmdreader

def stream(period):
    
    cmd = ['/usr/bin/iostat', '-xnz', str(period)]
    return cmdreader.stream(cmd, period)
