# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        nums.append(0)
        first = []
        second = []
        
        l1, r1 = 0, firstLen
        l2, r2 = 0, secondLen
        sum1, sum2 = sum(nums[:firstLen]), sum(nums[:secondLen])
        
        while r1 < len(nums) or r2 < len(nums):
            if r1 < len(nums):
                first.append((sum1, l1, r1 - 1))
                sum1 -= nums[l1]
                sum1 += nums[r1]
                l1 += 1
                r1 += 1
                
            if r2 < len(nums):
                second.append((sum2, l2, r2 - 1))
                sum2 -= nums[l2]
                sum2 += nums[r2]
                l2 += 1
                r2 += 1
                
        first.sort(reverse=True)
        second.sort(reverse=True)
        
        @cache
        def findMax(idx1, idx2):
            if idx1 >= len(first) or idx2 >= len(second):
                return -1
            
            if second[idx2][1] <= first[idx1][1] <= second[idx2][2]:
                return max(findMax(idx1 + 1, idx2), findMax(idx1, idx2 + 1))
            
            if first[idx1][1] <= second[idx2][1] <= first[idx1][2]:
                return max(findMax(idx1 + 1, idx2), findMax(idx1, idx2 + 1))
            
            return first[idx1][0] + second[idx2][0]
        
        return findMax(0, 0)
    
