n, t = [int(i) for i in input().split()]
s = list(input())
for _ in range(t):
    i = 1
    while i < n:
        if s[i] == 'G' and s[i-1] == 'B':
            s[i], s[i-1] = s[i-1], s[i]
            i += 1
        i += 1

print(''.join(s))
