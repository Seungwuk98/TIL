s = 'asdf?    ?   asdfasdfdfsf? dfd?Fs?Dfs?D? a?Sdf?asdf??   ?Asdf A?Sdf'
s = s.lower()

result = ''
for x in s:
    if x != ' ':
        result += x

p = ""
result2 = ''
for x in result:
    if p in '?!.,' and x not in '?!,.':
        result2 += ' '
    result2 += x
    p = x
result = result2.split()
result[0] = result[0].capitalize()
for i in range(1, len(result)):
    if result[i-1][-1] in '?!,.':
        result[i] = result[i].capitalize()

print(' '.join(result))
