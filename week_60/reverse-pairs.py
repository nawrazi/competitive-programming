# https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0
        
        def merge(nums):
            nonlocal pairs
            if len(nums) == 1:
                return nums
            
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            merged = []
            
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    merged.append(left[l])
                    pairs += bisect_left(right, left[l] / 2)
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
                    
            while l < len(left):
                merged.append(left[l])
                pairs += bisect_left(right, left[l] / 2)
                l += 1
                
            while r < len(right):
                merged.append(right[r])
                r += 1
                
            return merged
        
        merge(nums)
        return pairs
    
