from collections import defaultdict

def solve(nums):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
        if count[num] >= 3:
            print(num)
            return

    print(-1)


t = int(input())
for _ in range(t):
    n = input()
    nums = [int(i) for i in input().split()]
    solve(nums)
