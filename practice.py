
for i in range(10):
    s1 = []
    with open('answers/answer_{}.txt'.format(i), 'r') as f:
        s1 = f.readlines()
    s2 = []
    with open('output1/output_{}.txt'.format(i), 'r') as f:
        s2 = f.readlines()
    print(*[(s1[x], s2[x], x) for x in range(len(s1)) if s1[x] != s2[x]])
