# https://codeforces.com/gym/403606/problem/A

n = input()
a = ''
i = 0
if n[0] == '9':
    i += 1
    a += '9'

for c in n[i:]:
    if int(c) >= 5:
        a += str(9 - int(c))
    else:
        a += c

print(a)
