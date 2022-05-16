from random import randint

n = 10
arr = [randint(1, 10) for _ in range(n)]
m = 10
print(n)
print(*arr)
print(m)
for _ in range(m):
    op = randint(1, 10) & 1
    i, j = [randint(1, 10) for _ in range(2)]
    if i > j:
        i, j = j, i
    if op:
        x, y = [randint(1, 10) for _ in range(2)]
        print(op, i, j, x, y)
    else:
        print(i, j)
