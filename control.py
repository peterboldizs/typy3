__author__ = 'marti'

age = 27

if (age > 21):
    print("good to go")
if age > 25:
    print("very good")
else:
    print("too young")

name1 = "Peter"
name2 = "Lucy"
if name1 is not "Peter":
    print("Hi " + name1)
if name2 is "Lucy":
    print("doh")
elif name2 is not "Lucy":
    print("doh")
else:
    print("who are you?")

food = ['beer', 'wine', 'ham', 'eggs', "potato", "sausages"]
for f in food:
    print(f, len(f))
    #print(len(f))
print("how many items? ")
print(len(food))

for f in food[:4]:
    print(f)

for x in range(8):
    print(x, sep=',', end='\t')

print("\nsecond list: ")
for x in range(8, 16):
    print(x, sep=',', end='\t')

print("\nthird list: ")
for x in range(8, 28, 2):
    print(x, sep=',', end='\t')

print("\nwhile")
x = 9
while x < 15:
    print(x)
    x += 1

magic = 6
for j in range(1, 8):
    print("maybe ", j)
    if j == 2:
        continue
    print(j)
    if j == magic:
        print(j, " is the one!")
        break

print("divisible by eight:")
for k in range(100):
    if (k % 8 == 0):
        print(k)

numTaken = [2,4,6,8]
for n in range(15):
    if n in numTaken:
        print(n," taken")
        continue
        print("this should not print")
    print(n, " free")

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("sample1.txt"):
    print(line, end='')

s = 'qwertzu'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
