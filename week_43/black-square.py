# https://codeforces.com/gym/407909/problem/A

a = [int(i) for i in input().split()]
s = list(input())
t = 0
for c in s:
    t += a[int(c) - 1]

print(t)
