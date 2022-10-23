# https://codeforces.com/gym/405511/problem/C

n = int(input())
h1 = [int(i) for i in input().split()]
h2 = [int(i) for i in input().split()]

best = [0, 0]
prev = [0, 0]
for i in range(n - 1, -1, -1):
    prev = best.copy()
    best[0] = max(best[0], prev[1] + h1[i])
    best[1] =  max(best[1], prev[0] + h2[i])

print(max(best))
