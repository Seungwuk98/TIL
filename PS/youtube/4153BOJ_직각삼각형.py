while True:
    a, b, c = sorted(list(map(int, input().split())))
    if not a:
        break
    print('right' if c**2 == a**2 + b**2 else 'wrong')
