__author__ = 'fnxuser'

class Complex:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart

x = Complex(3.0, -4.5)
print(x.r, x.i)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def bark(self, word):
        print("woof {} - {}".format(self.name, word))

d = Dog('Fido')
f = Dog('Dido')
d.add_trick('yell')
d.add_trick('bark')
f.add_trick('bark')

print(d.kind, d.name, d.tricks)
print(f.kind, f.name, f.tricks)

d.bark("Haha")
f.bark("Hihi")

class SleepingDog(Dog):

    def sllleep(self):
        print("hrrr")

sl = SleepingDog('Budo')
sl.bark("wudo")
sl.sllleep()


