# https://codeforces.com/problemset/problem/1/A

(m,n,a) = [int(n) for n in input().split()]

m += a - m%a if m%a!=0 else 0
n += a - n%a if n%a!=0 else 0

print((m*n) // (a**2))
