# cmd reader iterator
import subprocess

def get_stream(cmd, period):
    
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE) 

    def iterator():
        for line in iter(p.stdout.readline, ''):
            yield line
    
    class Stream:
        def __init__(self):
            self.period = period
            self.it = iterator()
            self.p = p
        def close(self):
            self.p.stdout.close()
            self.p.kill()

    return Stream()
