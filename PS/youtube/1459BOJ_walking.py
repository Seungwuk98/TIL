x, y, w, s = map(int, input().split())
if 2*w <= s:
    print(w*(x+y))
else:
    if x > y:
        x, y = y, x
    print(s*x + w*(y-x))
