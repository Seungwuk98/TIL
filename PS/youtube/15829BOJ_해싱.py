n = int(input())
s = input()
r = 31
m = 1234567891
result = 0
a = 1
for x in s:
    result = (result + (ord(x)-96)*a) % m
    a = (a*r) % m
print(result)
