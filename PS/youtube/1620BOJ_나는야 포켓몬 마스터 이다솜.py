import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
a = ['']
for i in range(1, n+1):
    s = input().strip('\n')
    d[s] = i
    a.append(s)

for _ in range(m):
    s = input().strip('\n')
    try:
        s = int(s)
        print(a[s])
    except:
        print(d[s])
