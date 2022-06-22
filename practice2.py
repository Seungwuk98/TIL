x = 52

s1 = [input() for _ in range(x)]
s2 = [input() for _ in range(x)]
print(*[(s1[i], s2[i], i) for i in range(x) if (s1[i] != s2[i])], sep='\n')
