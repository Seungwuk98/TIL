s1 = []
s2 = []
for i in range(10):
    s1.append(input())
for i in range(10):
    s2.append(input())

for i in range(10):
    if s1[i] != s2[i]:
        print(i)
