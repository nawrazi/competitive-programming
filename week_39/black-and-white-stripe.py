# https://codeforces.com/contest/1690/problem/D

t = int(input())
for _ in range(t):
    n, k = [int(n) for n in input().split()]
    s = input() + ' '
    w, b = 0, 0
    l, r = 0, 0
    for _ in range(k):
        if s[r] == 'B':
            b += 1
        else:
            w += 1
        r += 1

    best = w
    while r < n + 1:
        if s[l] == 'W':
            w -= 1
        elif s[l] == 'B':
            b -= 1
        
        if s[r] == 'W':
            w += 1
        elif s[r] == 'B':
            b += 1
        else:
            r += 1
            continue

        l += 1
        r += 1

        best = min(best, w)

    print(best)
    
