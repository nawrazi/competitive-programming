# https://codeforces.com/gym/407909/problem/C

ff = {}
bb = {}
ids = []
n = int(input())
for _ in range(n):
    f, b = [int(i) for i in input().split()]
    ids.append(f)
    ids.append(b)
    bb[b] = f
    ff[f] = b

q = [0 for _ in range(n)]
for i in ids:
    if i not in ff:
        q[-1] = i
    if i not in bb:
        q[0] = i

one = ff[0]
two = ff[q[0]]
idx1 = 1
idx2 = 2
while idx2 < n:
    q[idx1] = one
    q[idx2] = two
    if one in ff and two in ff:
        one = ff[one]
        two = ff[two]
    else:
        break
    idx1 += 2
    idx2 += 2

print(*q)
