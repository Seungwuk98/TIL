from random import randint

n = 10
s = set()
while (len(s) < n):
    s.add((randint(-20, 20), randint(-20, 20)))

print(n)
for x in s:
    print(*x)
