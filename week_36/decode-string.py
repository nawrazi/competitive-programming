# https://codeforces.com/contest/1729/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    o = []
    i = n - 1
    while i >= 0:
        if s[i] != '0':
            o.append(chr(int(s[i]) + 96))
            i -= 1
        else:
            o.append(chr(int(s[i-2] + s[i-1]) + 96))
            i -= 3

    print(''.join(list(reversed(o))))
    
