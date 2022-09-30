# https://codeforces.com/contest/1690/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(n) for n in input().split()]
    b = [int(n) for n in input().split()]
    d = [ai - bi for ai, bi in zip(a, b)]

    s = set()
    f = True
    for i in range(n):
        if d[i] < 0:
            f = False
            break
        if b[i] == 0:
            continue
            
        s.add(d[i])

    if len(s) > 1 or not f:
        print('NO')
        continue

    s = list(s)
    if not s:
        print('YES')
        continue

    for i in range(n):
        if b[i] != 0:
            continue
        if d[i] > s[0]:
            f = False
            break

    print('YES' if f else 'NO')
    
