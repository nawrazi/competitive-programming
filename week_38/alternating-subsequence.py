# https://codeforces.com/gym/401249/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(n) for n in input().split()] + [0]
    ans = 0
    cur = nums[0]
    for i, num in enumerate(nums[:-1]):
        prev = nums[i - 1]
        if (num > 0 and prev < 0):
            ans += cur
            cur = nums[i]
        elif (num < 0 and prev > 0):
            ans += cur
            cur = num
        cur = max(cur, num)

    print(ans + cur)
    
