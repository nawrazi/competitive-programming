# https://codeforces.com/contest/1690/problem/A

from math import ceil, floor

t = int(input())
for _ in range(t):
    n = int(input())
    best = []
    for one in range(n - 3, -1, -1):
        left = n - one
        if left % 2 == 1:
            two = ceil(left / 2)
            three = floor(left / 2)
        else:
            two = (left // 2) + 1
            three = (left // 2) - 1

        if two >= one:
            break
        else:
            best = [two, one, three]

    print(*best)
    
