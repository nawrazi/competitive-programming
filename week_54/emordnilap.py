# https://codeforces.com/contest/1777/problem/B

from math import factorial

for _ in range(int(input())):
    n = int(input())
    print((factorial(n) * n * (n - 1)) % (pow(10, 9) + 7))
    
