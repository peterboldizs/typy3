__author__ = 'fnxuser'
import fibo
import sys
import builtins

fibo.fib(1000)
k = fibo.fib2(int(sys.argv[1]))
print("k is", k)
print(sys.platform)
print("####################\nsys.path")
for p in sys.path:
    print(p)
print("####################\ndir(sys)")
for d in dir(sys):
    print(d)
print("####################\nbuiltins")
for b in dir(builtins):
    print(b)
