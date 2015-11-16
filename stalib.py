__author__ = 'fnxuser'
import os
import shutil
import glob
import sys
import re
import math
import random
import statistics
from datetime import date

print(os.getcwd())
# for p in (dir(os)):
#    print(p)
os.chdir('/home/fnxuser/pytest')
# os.system('touch testfile1.txt')
os.system('date >> testfile2.txt')
shutil.copyfile('testfile2.txt', 't2.txt')
os.chdir('/home/fnxuser/PycharmProjects/typy3')
for pf in glob.glob('*.py'):
    print(pf)

sys.stdout.write('\nsomething to the standard output')
sys.stderr.write('\nsomething to the standard error')
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print("mathematics")
print(math.cos(math.pi / 4))
print(math.log(1024, 2))
print(random.choice(['a', 'b', 'c']))
print(random.sample(range(100), 5))
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
print("date-time")
now = date.today()
print(now)
print(now.strftime("%y. %m. %d"))
print(now.strftime("%Y. %B %d,  %A"))
