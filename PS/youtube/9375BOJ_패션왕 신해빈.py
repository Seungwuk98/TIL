for _ in range(int(input())):
    d = {}
    for __ in range(int(input())):
        cloth, typ = input().split()
        if typ not in d:
            d[typ] = 1
        else:
            d[typ] += 1

    result = 1
    for val in d.values():
        result *= val+1
    print(result-1)
