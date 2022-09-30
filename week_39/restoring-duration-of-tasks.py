# https://codeforces.com/contest/1690/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(n) for n in input().split()]
    f = [int(n) for n in input().split()]

    cur = 0
    d = []
    for i in range(n):
        d.append(f[i] - max(cur, s[i]))
        cur = f[i]

    print(*d)
    
