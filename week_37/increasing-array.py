# https://cses.fi/problemset/task/1094

n = int(input())
nums = [int(n) for n in input().split()]
cur = nums[0]
moves = 0
for i in range(1, n):
    if nums[i] < cur:
        moves += cur - nums[i]
    else:
        cur = nums[i]

print(moves)
