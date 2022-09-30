# https://codeforces.com/gym/401249/problem/A

n, t = [int(n) for n in input().split()]
books = [int(n) for n in input().split()]
r = 0
i = 0
for c in books:
    r += c
    if (r > t):
        r -= books[i]
        i += 1

print(n - i)
