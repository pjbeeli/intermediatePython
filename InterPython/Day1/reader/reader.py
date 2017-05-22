import os

from Day1.reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2':bzipped.opener,
    '.bz2':bzipped.opener,
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        #self.filename = filename
        self.f = opener(filename, "rt")

    def close(self):
         self.f.close()


    def read(self):
        return self.f.read()


def main():
    pass
