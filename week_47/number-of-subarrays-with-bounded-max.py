# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        valley = [[0, 0] for _ in nums]
        
        stack = []
        for i, num in enumerate(nums + [inf]):
            cur = [i, 0]
            while stack and num >= nums[stack[-1][0]]:
                idx, val = stack.pop()
                valley[idx][0] += val
                cur[1] += 1 + val
                
            stack.append(cur)
            
        stack = []
        for i, num in enumerate(reversed([inf] + nums)):
            cur = [len(nums) - i - 1, 0]
            while stack and num > nums[stack[-1][0]]:
                idx, val = stack.pop()
                valley[idx][1] += val
                cur[1] += 1 + val
                
            stack.append(cur)
            
        count = 0
        for i, num in enumerate(nums):
            if left <= num <= right:
                count += (valley[i][0] + 1) * (valley[i][1] + 1)
        
        return count
    
