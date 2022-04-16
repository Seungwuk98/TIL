from random import randint
INF = (1 << 31)-1
MINF = -(1 << 31)

i = 10
while i <= 100000000:
    print(i)
    print(*[randint(MINF, INF)for _ in range(i)])
    print(randint(1, i))
    i *= 10
