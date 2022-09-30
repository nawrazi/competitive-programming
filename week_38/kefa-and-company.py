# https://codeforces.com/gym/401249/problem/C

n, d = [int(n) for n in input().split()]
friends = []
for i in range(n):
    m, f = [int(n) for n in input().split()]
    friends.append((m, f))

friends.sort()
fac = friends[0][1]
total = fac
i, j = 0, 1
while j < n:
    if friends[j][0] - friends[i][0] < d:
        fac += friends[j][1]
        total = max(total, fac)
    else:
        fac -= friends[i][1]
        i += 1
        j -= 1
    j += 1

print(total)
