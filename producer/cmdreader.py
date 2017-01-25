# cmd reader iterator
import subprocess
import sys

def get_stream(cmd, period, name='cmdreader'):
    
    p = subprocess.Popen(cmd, stdin=None, stdout=subprocess.PIPE, stderr=None) 

    def iterator():
        for line in iter(p.stdout.readline, ''):
            yield line
    
    class Stream:
        def __init__(self):
            self.period = period
            self.it = iterator()
            self.p = p
        def close(self):
            sys.stderr.write('Stoping producer: {0} ...\n'.format(name))
            self.p.stdout.close()
            self.p.kill()
            self.p.wait()

    return Stream()
