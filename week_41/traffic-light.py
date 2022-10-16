# https://codeforces.com/contest/1744/problem/C

t = int(input())
for _  in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    on = None
    dist = 0
    if c == 'g':
        print(0)
        continue
        
    for i, l in enumerate(s):
        if l == c and on is None:
            on = i
        elif l == 'g' and on is not None:
            dist = max(dist, i - on)
            on = None

    if on is not None:
        dist = max(dist, s.find('g') + (n - on))

    print(dist)
    
