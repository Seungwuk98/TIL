import sys
from collections import defaultdict
input = sys.stdin.readline
N = 1000000
SN = 1000
mpf = [*range(N+1)]


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r *= c
        c *= c
        n >>= 1
    return r


for i in range(2, SN):
    if mpf[i] == i:
        for j in range(i*i, N+1, i):
            if mpf[j] == j:
                mpf[j] = i

pre = [0, 1]
for i in range(2, N+1):
    x = i
    factorize = defaultdict(int)
    while x != 1:
        factorize[mpf[x]] += 1
        x //= mpf[x]
    result = 1
    for y in factorize:
        result *= (pow(y, factorize[y]+1)-1)//(y-1)
    pre.append(pre[-1]+result)

for _ in range(int(input())):
    print(pre[int(input())])
