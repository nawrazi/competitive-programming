# https://codeforces.com/gym/394494/problem/A

n, k = [int(i) for i in input().split()]
total = 0
for _ in range(n):
    num = set(input())
    good = True
    for i in range(k + 1):
        if str(i) not in num:
            good = False
            break
    if good:
        total += 1

print(total)
