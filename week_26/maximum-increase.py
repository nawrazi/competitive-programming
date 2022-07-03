_ = int(input())
nums = [int(i) for i in input().split()] + [0]

max_len = 1
i, j = 0, 1

while j < len(nums):
    if nums[j] <= nums[j-1]:
        max_len = max(max_len, j - i)
        i = j
    j += 1

print(max_len)