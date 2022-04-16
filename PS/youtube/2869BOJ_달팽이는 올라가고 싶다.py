a, b, v = map(int, input().split())
q, r = divmod(v-a, a-b)
print(q+1 if not r else q+2)
