import re

def get_iterator(it, discard_first=False):

    timestamp = re.compile('^\d{10}$')
    chunck = []

    for line in it:
        if timestamp.match(line) and chunck: # not first occurence of timestamp

            if discard_first: # discard the first chunck (aggregate stat)
                discard_first = False
                chunck = [line]
                continue

            yield chunck 
            chunck = [line]
        else:
            chunck.append(line)
