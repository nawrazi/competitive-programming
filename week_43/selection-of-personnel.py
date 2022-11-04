# https://codeforces.com/problemset/problem/630/F

from math import factorial

def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

n = int(input())
print(combination(n, 5) + combination(n, 6) + combination(n, 7))
