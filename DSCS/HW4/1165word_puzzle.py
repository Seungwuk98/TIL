root = []
n = 24830
for _ in range(n):
    s = input()
    root.append(s)

inc = [[]for _ in range(20)]
for i in range(20):
    for j in range(n):
        try:
            inc[i].append(root[j][i])
        except:
            inc[i].append('')

real = [[]for _ in range(20)]
for i in range(20):
    l = 0
    for j in range(n):
        if j and inc[i][j] != inc[i][j-1]:
            real[i].append((inc[i][j], l))
            l = 0
        l += 1
    real[i].append((inc[i][j], l))

for x in real:
    print(x)
