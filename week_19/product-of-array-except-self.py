# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_bef = {-1 : 1}
        prod_aft = {n : 1}

        for i in range(n):
            prod_bef[i] = prod_bef[i-1] * nums[i]
            prod_aft[n-i-1] = prod_aft[n-i] * nums[n-i-1]

        return [prod_bef[i-1] * prod_aft[i+1] for i in range(n)]
