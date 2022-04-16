import sys
input = sys.stdin.readline

k = int(input())
s = []
for _ in range(k):
    x = int(input())
    if x:
        s.append(x)
    else:
        s.pop()

print(sum(s))
