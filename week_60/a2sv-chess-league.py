# https://codeforces.com/gym/430380/problem/E

def merge(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = merge(nums[:mid])
    right = merge(nums[mid:])
    win = []
    ml, mr = min(left, key=lambda x:x[0])[0], min(right, key=lambda x:x[0])[0]
    
    for num, idx in left:
        if num > mr or mr - num <= k:
            win.append((num, idx))
            
    for num, idx in right:
        if num > ml or ml - num <= k:
            win.append((num, idx))
            
    return win

_, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
nums = [(num, i) for i, num in enumerate(nums)]
res = merge(nums)
print(*[idx + 1 for _, idx in res])
