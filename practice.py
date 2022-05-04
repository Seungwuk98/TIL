from random import randint
from bisect import *


s = []
n = 30

ret = []
order = []
for _ in range(n):
    op = 'IIIIIIDDDSR'[randint(0, 10)]
    x = randint(1, 50)
    if op == 'I':
        if x not in s:
            insort_left(s, x)
        order.append((op, x))
    elif op == 'D':
        if x in s:
            s.remove(x)
        order.append((op, x))
    else:
        if op == 'S' and randint(0, 9) % 2 and s:
            x = s[randint(0, len(s)-1)]
        order.append((op, x))

for x in order:
    print(*x)

s = []
for i in range(n):
    op, x = order[i]
    if op == 'I':
        if x in s:
            print(0)
        else:
            insort_left(s, x)
            print(x)
    elif op == 'D':
        if x not in s:
            print(0)
        else:
            s.remove(x)
            print(x)
    elif op == 'S':
        if x > len(s) or x <= 0:
            print(0)
        else:
            print(s[x-1])
    else:
        if x in s:
            print(bisect_left(s, x)+1)
        else:
            print(0)
