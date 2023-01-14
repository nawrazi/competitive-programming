# https://codeforces.com/problemset/problem/300/A

input()
arr = [int(i) for i in input().split()]
n, p, o = set(), set(), set()

for a in arr:
    if a > 0 and not p:
        p.add(a)
    elif a < 0 and not n:
        n.add(a)
    else:
        o.add(a)

if not p:
    for _ in range(2):
        m = min(o)
        p.add(m)
        o.remove(m)

print(len(n), *n)
print(len(p), *p)
print(len(o), *o)
