# https://codeforces.com/gym/400361/problem/A

n = int(input())
s = [int(n) for n in input().split()]
mx = max(s)
mn = min(s)
t = 0
for c in s:
    if c != mx and c != mn:
        t += 1

print(t)
