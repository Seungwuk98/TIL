import sys
input = sys.stdin.readline
n, m = map(int, input().strip('\n').split())
a = {input().strip('\n')for _ in range(n)}
b = {input().strip('\n')for _ in range(m)}
c = sorted(list(a & b))
print(len(c))
for x in c:
    print(x)
