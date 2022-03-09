# https://codeforces.com/problemset/problem/1646/B

def solve(nums):
    blues, reds = nums[0], 0
    output = 'NO'

    b, r = 1, len(nums) - 1
    while b < r:
        blues += nums[b]
        reds += nums[r]
        b += 1
        r -= 1
        if reds > blues:
            output = 'YES'
            break

    print(output)


t = int(input())
for _ in range(t):
    _ = int(input())
    nums = sorted([int(i) for i in input().split()])

    solve(nums)
