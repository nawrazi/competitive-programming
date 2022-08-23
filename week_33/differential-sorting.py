# https://codeforces.com/contest/1635/problem/C

def solve():
    _ = input()
    arr = [int(i) for i in input().split()]
    if arr[-1] < arr[-2]:
        print(-1)
        return
    i = len(arr) - 3
    moves = []
    while i >= 0:
        long_diff = arr[i + 1] - arr[-1]
        short_diff = arr[-2] - arr[-1]
        if arr[i] > arr[i + 1]:
            if long_diff <= arr[i + 1]:
                moves.append([i + 1, i + 2, len(arr)])
                arr[i] = long_diff
            elif short_diff <= arr[i + 1]:
                moves.append([i + 1, len(arr) - 1, len(arr)])
                arr[i] = short_diff
            else:
                print(-1)
                return
        i -= 1

    print(len(moves))
    for i in range(len(moves)):
        print(*moves[i])

t = int(input())
for _ in range(t):
    solve()
