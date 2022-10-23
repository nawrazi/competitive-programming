# https://codeforces.com/gym/405511/problem/A

n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
i = 0
j = k
h = sum(nums[:k])
best = 1, h
while j < n:
    h -= nums[i]
    h += nums[j]
    i += 1
    j += 1
    if h < best[1]:
        best = i + 1, h

print(best[0])
