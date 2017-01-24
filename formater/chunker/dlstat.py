import re

def get_iterator(it):

    timestamp = re.compile('^\d{10}$')
    chunck = []
    first = True

    for line in it:
        if timestamp.match(line) and chunck: # not first occurence of timestamp

            if first: # discard the first chunck (aggregate stat)
                first = False
                chunck = [line]
                continue

            yield chunck 
            chunck = [line]
        else:
            chunck.append(line)
