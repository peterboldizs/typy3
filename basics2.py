__author__ = 'peter'
###################################################
print("basics")
a = 10
b = 202
c = a + b
d, e, f = 2, 3, 4
name = 'Peter'
print(c)
print(name, len(name))
print(d,e,f)
g = None
print(g)

###################################################
print("collections")
dict = {'name': 'peter', 'id': 10, 'dept': 'it'}
print(dict.keys())
print(dict.values())
tuple = ('rahul', 100, 60.4, 'deepak')
print(tuple)
list1 = ['aman', 678, 20.4, 'saurav',202]
print(list1)
print(list1[1:4])
print(list1 * 3)

###################################################
print("operators")
if(a in list1):
    print("a is in list")
else:
    print("a is NOT in list")
if(b in list1):
    print("b is in list")
else:
    print("b is NOT in list")

if(a is b):
    print("they are the same")
else:
    print("they are different")

###################################################
print("loops, ranges")
#t3 = (1,2,3,4,5,6)
list2 = []
for i in range(2,10):
    j = a * i
    #print(j)
    list2.append(j)

print("list2:\n", list2)

for j in range (1,6):
    for k in range (5,j-1,-1):
        print("*"),
    print

a=10
while a>0:
    print ("Value of a is",a)
    #a=a-2
    a -= 2

###################################################
print("typecasting")
a=10
b="10"
c="20"
print(int(b) + a)
print(b+c)

###################################################
print("basic ops:")
print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (3 % 2)
print (3 ** 4) # 3 to the fourth power
print (3 // 4) #floor division
