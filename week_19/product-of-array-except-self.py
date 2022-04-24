# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_bef = {-1 : 1}
        prod_aft = {len(nums) : 1}

        for i in range(len(nums)):
            prod_bef[i] = prod_bef[i-1] * nums[i]
            prod_aft[len(nums)-i-1] = prod_aft[len(nums)-i] * nums[len(nums)-i-1]

        return [prod_bef[i-1] * prod_aft[i+1] for i in range(len(nums))]
