# https://leetcode.com/problems/arithmetic-subarrays/

def checkArithmeticSubarrays(nums, l, r):
    n = len(l)
    final = []
    for i in range(n):
        sub = nums[l[i]:r[i]+1]
        sub.sort()
        m = len(sub)
        arithmetic = True
        for j in range(m-1):
            if sub[j+1] - sub[j] == sub[1] - sub[0]:
                continue
            arithmetic = False
            break

        final.append(arithmetic)

    return final
