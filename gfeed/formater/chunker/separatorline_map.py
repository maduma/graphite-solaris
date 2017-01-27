import separatorline

def get_iterator(lines, pattern, transform):

    chunks = separatorline.get_iterator(lines, pattern)

    def iterator():
        for chunk in chunks:
            for line in transform(chunk):
                yield line

    return iterator()
