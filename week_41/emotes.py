# https://codeforces.com/group/b5GBy1CJ0d/contest/368852/problem/B

n, m, k = [int(n) for n in input().split()]
arr = sorted([int(n) for n in input().split()])
div = m // (k + 1)
rem = m % (k + 1)
print((k * arr[-1] * div) + (arr[-2] * div) + (rem * arr[-1]))
