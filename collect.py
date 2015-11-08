__author__ = 'marti'

import functions
import random

#lists
players = [12, 23, 45, 56, 67]
print(players)
print(players[2])
players[2] = 32
print(players)
players += [90,92,98]
print(players)
players.append(100)
print(players)
players[:2] = [0,0]
print(players)
players[:2] = []
print(players)

#sets
groceries = {'ham', 'apples', 'eggs', 'wine', 'wine', "milk"}
print(groceries)
if 'milk' not in groceries:
    print("you need milk")
else:
    print("already have milk", len(groceries))

#dictionaries
dict = {'name': 'peter', 'id': 10, 'dept': 'it'}
print(dict.keys())
print(dict.values())
print(dict.get('id'))

for k,v in dict.items():
    print(k, "=>", v)


#importing a module
print('from import:')
print(functions.usd_to_huf(15))

x = random.randrange(1,100)
print(x)