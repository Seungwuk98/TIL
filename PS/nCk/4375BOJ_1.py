import sys


def check(n):
    r = 1
    ret = 1
    while r % n:
        r *= 10
        r += 1
        ret += 1
    return ret


for x in sys.stdin.readlines():
    print(check(int(x)))
