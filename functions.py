__author__ = 'peter'

def my_first():
    """

    :rtype : object
    """
    print("Hello" + " ok")

for i in range(5):
    my_first()

def usd_to_huf(usd):
    amount= usd * 254
    return amount

print(18, "usd is", usd_to_huf(18), "huf")

#default params
def get_gender(sex='Unknown'):
    gender = "n"
    if sex is "m":
        gender = "Male"
    elif sex is "f":
        gender = "Female"
    print(sex,gender)

get_gender("n")
get_gender()
get_gender("m")
get_gender("f")

# variable scope
a = 1

def corn():
    a = 25
    print(a)
    print(b)

b = 5

def fudge():
    print(a)

corn()
fudge()

def dumb(name='Peter', action='goes', item='apple'):
    print(name,action,item)

dumb()
dumb("Jack", "stays", "home")
dumb(name="John")
dumb(item="beer")

#variable arguments
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print("sum", total)

add_numbers(1,2,3,4,5)
add_numbers(4,5,6,7)

#unpacking arguments from a list
def health(age, apples, cigs):
    answer = (100 - age) + (apples * 3.5) - (cigs * 2)
    print("your health", answer)

health(23,12,5)

peter_data =[34, 23, 12]
health(peter_data[0], peter_data[1], peter_data[2])
health(*peter_data)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)

    print("#" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

    print("-" * 40)

cheeseshop("maci", ["sajnos","nincs", "több"], {"a": "Peter", "b": "BOldizs"})


def make_inc(n):
    return lambda  x: x+n

f = make_inc(40)

print(f(0))
print(f(11))