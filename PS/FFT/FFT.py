from math import *


def doFFT(a, w):
    n = len(a)
    if n == 1:
        return
    even = a[0::2]
    odd = a[1::2]

    doFFT(even, w*w)
    doFFT(odd, w*w)
    wp = 1+0j
    for i in range(n//2):
        a[i] = even[i] + wp*odd[i]
        a[i+n//2] = even[i] - wp*odd[i]
        wp *= w


def multiply(a, b):
    n = 1
    al, bl = len(a), len(b)
    while (n < al+1 or n < bl+1):
        n <<= 1
    while len(a) < n:
        a.append(0)
    while len(b) < n:
        b.append(0)

    w = complex(cos(2*pi/n), sin(2*pi/n))
    doFFT(a, w)
    doFFT(b, w)
    c = []
    for i in range(n):
        c.append(a[i]*b[i])

    doFFT(c, w.conjugate())
    for i in range(n):
        c[i] /= n
        c[i] = int(round(c[i].real))
    return c


def mul(x, y):
    a = [int(i) for i in x[::-1]]
    b = [int(i) for i in y[::-1]]
    c = multiply(a, b)
    c.append(0)
    for i in range(len(c)-1):
        q, r = divmod(c[i], 10)
        c[i+1] += q
        c[i] = r
    while c[-1] == 0:
        c.pop()
    return ''.join(map(str, c[::-1]))
