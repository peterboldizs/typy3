__author__ = 'marti'
import math

s = 'Hello\n world'
print(str(s))
print(repr(s))

print("table of squares and cubes - 1")
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

print("table of squares and cubes - 2")
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print("some formatted printing")
print('12'.zfill(6))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.4f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print("reading from and writing to a file")
fw = open('sample1108.txt', 'w')
numchars = fw.write('this is a sample test\nAnd this is a new line')
fw.close()
print('file complete, {} chars written'.format(numchars))
print("read at once")
fr = open('sample1108.txt', 'r')
text = fr.read()
print(text)
fr.close()
print("read line by line")
fr = open('sample1108.txt', 'r')
print("first::>>",fr.readline())
print("next::>>",fr.readline())
fr.close()
print("read in loop")
fr3 = open('sample1108.txt', 'r')
for li in fr3:
    print(li,end=' ..')