# https://codeforces.com/contest/1729/problem/B

t = int(input())
for _ in range(t):
    a, b, c = [int(n) for n in input().split()]
    fir = abs(a - 1)
    sec = abs(b - c) + abs(c - 1)
    if fir < sec:
        print(1)
    elif fir > sec:
        print(2)
    else:
        print(3)
        
