# https://cses.fi/problemset/task/1071

t = int(input())
for _ in range(t):
    r, c = [int(n) for n in input().split()]
    mx, mn = max(r, c), min(r, c)
    start, end = ((mx - 1) ** 2) + 1, mx ** 2

    if mx % 2 == 1:
        if r < c:
            print(end - (r - 1))
        else:
            print(start + (c - 1))
    else:
        if r < c:
            print(start + (r - 1))
        else:
            print(end - (c - 1))
