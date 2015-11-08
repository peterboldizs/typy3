__author__ = 'fnxuser'
from collections import deque
from math import pi

print("using lists")
a = [66.25, 333, 333, 1, 1234.5]
print("append")
a.append(18)
print(a)
print("insert")
a.insert(0,2)
print(a)
print("del")
del a[2]
print(a)

print(a.index(333))
a.remove(1)
print(a)
a.sort()
print(a)
a.pop()
print(a)

print("using stacks - lifo")
st = [3,4,5]
st.append(6)
st.append(7)
print(st)
st.pop()
print(st)

print("using queues - fifo")
q = deque(["Eric", "John", "Michael"])
q.append("Terry")
q.append("Graham")
print(q)
print(q.popleft())
print(q)

sq = []
for x in range(10):
    sq.append(x ** 2)
print(sq)

cubes = [x**3 for x in range(10)]
print(cubes)

uelist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(uelist)

print("vector operations")
vec = [-4,-2,0,2,4,6]
vec2 = [x*2 for x in vec]
print(vec2)
print([x for x in vec if x > 0])
print([abs(x) for x in vec2])
print([(x,x**2) for x in range(10)])
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

print("tuples")
t = 1234,4321,'hello'
print(t)
u = t, (5,6,7,8)
print(u)

print("set")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
if 'apple' in basket:
    print("apple is in basket")

print('plus' in basket)
for f in sorted(set(basket)):
    print(f)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a ^ b)
print(a & b)
print({x for x in 'abracadabra' if x not in 'abc'})
print("dictionary")
tel = {'jack': 4098, 'sape': 4139}
tel['peter'] = 8827
print(tel)
print(sorted(tel.keys()), tel.values())
tel2 = dict([('a',1), ('b', 2), ('c', 3)])
print(tel2)
for k,v in tel.items():
    print(k,"=>",v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))