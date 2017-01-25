# cmd reader iterator
import subprocess
import sys

def get_stream(cmd, period, name='cmdreader'):
    
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None) 

    def iterator():
        for line in iter(p.stdout.readline, ''):
            yield line
    
    class Stream:
        def __init__(self):
            self.period = period
            self.it = iterator()
            self.p = p
        def close(self):
            msg = 'Stoping producer: {0} ...\n'.format(name)
            sys.stderr.write(msg)
            self.p.stdout.close()
            self.p.kill()
            self.p.wait()

    return Stream()
