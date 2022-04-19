def solve(rows, cols):
    if min(rows, cols) == 1 and max(rows, cols) > 2:
        return -1

    if abs(rows - cols) % 2 == 1:
        return 2 * max(rows, cols) - 3
    else:
        return 2 * max(rows, cols) - 2


t = int(input())
for _ in range(t):
    rows, cols = [int(i) for i in input().split()]
    print(solve(rows, cols))
