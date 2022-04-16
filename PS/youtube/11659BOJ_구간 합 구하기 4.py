import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0]
for x in arr:
    pre.append(pre[-1]+x)

for _ in range(m):
    i, j = map(int, input().split())
    print(pre[j]-pre[i-1])
