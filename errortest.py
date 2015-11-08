__author__ = 'fnxuser'

try:
    a = 10 * (1/0)
    print(a)
except ZeroDivisionError:
    print("ZeroDivisionError!!!")

try:
    b = 4 + spam*3
    print(b)
except NameError:
    print("NameError!!!")

try:
    raise Exception(1,2,'hello')
except Exception as ex:
    print(type(ex))
    print(ex.args)
finally:
    print("finally, bye")


def osztas(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("nullaval osztasz?")
    else:
        print("eredmény",result)
    finally:
        print("finally blokk")

osztas(10,2)
osztas(5,0)
