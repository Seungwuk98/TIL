from itertools import combinations_with_replacement

n = int(input())
sq = set()
x = 1
while x*x <= n:
    sq.add(x*x)
    x += 1

if n in sq:
    print(1)
    exit(0)

for x in sq:
    if n-x in sq:
        print(2)
        exit(0)

comb = combinations_with_replacement(sq, 2)

for x, y in comb:
    if n-x-y in sq:
        print(3)
        exit(0)

print(4)
