n = int(input())
for i in range(n):
    x = i
    r = i
    while x:
        r += x % 10
        x //= 10
    if r == n:
        break
else:
    print(0)
    exit(0)
print(i)
