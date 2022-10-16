# https://codeforces.com/group/b5GBy1CJ0d/contest/368852/problem/C

n, k = [int(n) for n in input().split()]
l = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]
old = 0
cur = 0
for i in range(n):
    if b[i] == 1:
        old += l[i]
    elif i < k:
        cur += l[i]

i, j = 0, k - 1
best = cur
while j < n - 1:
    if b[i] == 0:
        cur -= l[i]
    i += 1
    j += 1
    if b[j] == 0:
        cur += l[j]
    best = max(best, cur)

print(best + old)
