n = int(input())
people = [input().split()for _ in range(n)]
people.sort(key=lambda x: int(x[0]))

for x in people:
    print(' '.join(x))
