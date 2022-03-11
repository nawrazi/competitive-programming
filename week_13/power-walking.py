# https://codeforces.com/problemset/problem/1642/B

def solve(powers):
    seen = set()
    types = 0
    for power in powers:
        if power not in seen:
            types += 1
            seen.add(power)

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
