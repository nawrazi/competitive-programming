# https://cses.fi/problemset/task/1070

n = int(input())
if 1 < n < 4:
    print('NO SOLUTION')
    exit()

perm = []
for i in range(2, n + 1, 2):
    perm.append(i)

for i in range(1, n + 1, 2):
    perm.append(i)

print(*perm)
