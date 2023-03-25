# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/description/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]
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
                    pairs += len(right) - bisect_left(right, left[l] - diff)
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
                    
            while l < len(left):
                merged.append(left[l])
                pairs += len(right) - bisect_left(right, left[l] - diff)
                l += 1
                
            return merged + right[r:]
        
        merge(nums)
        return pairs
    
