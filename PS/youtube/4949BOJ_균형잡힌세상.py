
def check(a):
    s = []
    for x in a:
        if x == '(':
            s.append(x)
        elif x == ')':
            if not s or s[-1] != '(':
                return 'NO'
            else:
                s.pop()
    if s:
        return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    a = input()
    print(check(a))
