n, m = map(int, input().split())
isprime = [True]*(m+1)
isprime[0] = isprime[1] = False
for i in range(2, int(m**0.5)+1):
    if isprime[i]:
        for j in range(i*i, m+1, i):
            isprime[j] = False
prime = [x for x in range(n, m+1) if isprime[x]]
for y in prime:
    print(y)
