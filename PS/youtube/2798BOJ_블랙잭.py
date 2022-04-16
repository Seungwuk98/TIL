from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))
a_comb = combinations(a, 3)
result = 0
for x, y, z in a_comb:
    r = x+y+z
    if r <= m and result < r:
        result = r
print(result)
