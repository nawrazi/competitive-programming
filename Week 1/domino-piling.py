# https://codeforces.com/problemset/problem/50/A

(m,n) = [int(n) for n in input().split()]

if m%2!=0 and n%2!=0:
    dominoes = ((m-1)//2)*n + (n-1)//2
    print(dominoes)

elif m%2==0:
    dominoes = (m//2)*n
    print(dominoes)

elif n%2==0:
    dominoes = (n//2)*m
    print(dominoes)
