# https://codeforces.com/contest/1744/problem/B

t = int(input())
for _ in range(t):
    n, q = [int(n) for n in input().split()]
    arr = [int(n) for n in input().split()]
    tot = sum(arr)
    par = [0, 0]
    for a in arr:
        if a % 2:
            par[1] += 1
        else:
            par[0] += 1

    for _ in range(q):
        i, k = [int(n) for n in input().split()]
        tot += par[i] * k
        print(tot)
        if k % 2 == 1 and i == 1:
            par = [n, 0]
        if k % 2 == 1 and i == 0:
            par = [0, n]
            
