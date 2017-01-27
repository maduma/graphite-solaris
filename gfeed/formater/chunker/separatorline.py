import re

def get_iterator(it, pattern, discard_first):

    chunck = []

    for line in it:
        if pattern.match(line) and chunck: # not first occurence of pattern

            if discard_first: # discard the first chunck (aggregate stat)
                discard_first = False
                chunck = [line]
                continue

            yield chunck 
            chunck = [line]
        else:
            chunck.append(line)
