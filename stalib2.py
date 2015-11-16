__author__ = 'fnxuser'

import reprlib
import pprint
import textwrap
# import locale
from string import Template
import struct
import threading
import zipfile
import logging

logging.basicConfig(level=logging.INFO)

print(reprlib.repr(set('supercalifragilisticexpialidocious')))
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width=40))

# locale.setlocale(locale.LC_ALL, 'en_US')
# conv = locale.localeconv()
# x = 1234567.8
# print(locale.format("%d", x, grouping=True))

t = Template('${village} people send $$10 for $cause')
print(t.substitute(village='Budapest', cause='human aid'))
d = dict(village='Paris', cause='bargain')
print(t.substitute(d))

print("zip files")
with open('test.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start + extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        try:
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
        except FileNotFoundError:
            logging.ERROR('no such file')
        else:
            print('finished zip of ', self.infile)


bkg = AsyncZip('sample1.txt', 'sample1.zip')
bkg.start()
logging.info('main program is running...')
bkg.join()
logging.info('Main program waited until zip was done')
