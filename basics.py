__author__ = 'boldizsp'

#############################################################################
print('Fibonacci')


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()


# invoke
fib(200)

#############################################################################
print('\nWord list')

words = ['cat', 'bat', 'bicycle']
for w in words[:]:
    print(w, len(w))
    if len(w) > 6:
        words.insert(0, w)
print(words)

print('Ranges')
for i in range(0, 15, 3):
    print(i)
print(list(range(2, 28, 2)))

print('Primes')
#############################################################################


def primes(fro, to):
    for n in range(fro, to):
        for x in range(2, n):
            if n % x == 0:
                print(n, '=', x, '*', n // x)
                break
        else:
            print(n, 'is prime')


primes(1,30)

print('odd-even')
for num in range(2, 10):
    if num % 2 == 0:
        print('even:', num)
        continue
    print('odd:', num)

