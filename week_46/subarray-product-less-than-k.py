# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.append(1)
        i, j = 0, 0
        product = 1
        subarrays = 0
        
        while j < len(nums):
            if j < len(nums) - 1 and product * nums[j] < k:
                product *= nums[j]
                j += 1
            elif i < j:
                subarrays += j - i
                product //= nums[i]
                i += 1
            else:
                i += 1
                j += 1
                
        return subarrays
    
