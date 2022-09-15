# https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = (10 ** 9) + 7
        if len(nums) == 1:
            return (nums[0] + k) % mod
        
        heapify(nums)
        
        while k:
            num = heappop(nums)
            diff = min(nums[0] - num + 1, k)
            num += diff
            heappush(nums, num)
            k -= diff
            
        ans = 1
        for num in nums:
            ans = (ans % mod * num % mod) % mod
            
        return ans
    
