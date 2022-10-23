# https://codeforces.com/gym/405511/problem/B

n, k = [int(i) for i in input().split()]
s = input()
ab = [0, 0]
m = 0
l = 0
best = 0
for r in range(n):
    if s[r] == 'a':
        ab[0] += 1
        m = min(ab)
    else:
        ab[1] += 1
        m = min(ab)
    
    while m > k:
        if s[l] == 'a':
            ab[0] -= 1
            m = min(ab)
        else:
            ab[1] -= 1
            m = min(ab)
        l += 1

    best = max(best, r - l + 1)

print(best)
