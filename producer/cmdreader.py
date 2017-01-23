# cmd reader iterator
import subprocess

def stream(cmd, period):

    def iterator():
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('#'): continue
                yield line

    return { 'period': period, 'iterator': iterator() }
