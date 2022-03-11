# https://codeforces.com/problemset/problem/1642/B

def solve(powers):
    types = len(set(powers))
    final = []
    extra = 0
    for i, power in enumerate(powers):
        if i + 1 > types:
            extra += 1
        final.append(str(types + extra))

    print(' '.join(final))

t = int(input())
for _ in range(t):
    n = int(input())
    powers = [int(i) for i in input().split()]
    solve(powers)
