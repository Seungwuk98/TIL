n = int(input())
word = list({input()for _ in range(n)})
word.sort(key=lambda x: (len(x), x))
print('\n'.join(word))
