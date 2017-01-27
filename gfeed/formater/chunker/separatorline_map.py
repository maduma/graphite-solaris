import separatorline

def get_iterator(lines, pattern, transform, discard_first=True):

    chunks = separatorline.get_iterator(lines, pattern, discard_first)

    def iterator():
        for chunk in chunks:
            for line in transform(chunk):
                yield line

    return iterator()
