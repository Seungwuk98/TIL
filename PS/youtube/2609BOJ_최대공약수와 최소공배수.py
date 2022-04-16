a, b = map(int, input().split())


def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y % x, x
    return y


g = gcd(a, b)
print(g)
print(a*b//g)
