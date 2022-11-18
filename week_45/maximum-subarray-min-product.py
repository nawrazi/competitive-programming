# https://leetcode.com/problems/maximum-subarray-min-product/

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        limits = [[0, 0] for _ in nums]
        
        stack = []
        for i, num in enumerate(nums + [0]):
            cur = [num, i, 0]
            while stack and num <= stack[-1][0]:
                val, idx, pops = stack.pop()
                cur[2] += 1 + pops
                limits[idx][0] = pops
            stack.append(cur)
            
        stack = []
        for i, num in enumerate(nums[::-1] + [0]):
            cur = [num, len(nums) - i - 1, 0]
            while stack and num <= stack[-1][0]:
                val, idx, pops = stack.pop()
                cur[2] += 1 + pops
                limits[idx][1] = pops
            stack.append(cur)
            
        current = 0
        prefix = [0]
        for num in nums:
            current += num
            prefix.append(current)
            
        max_product = 0
        for i, (start, end) in enumerate(limits):
            sub_sum = prefix[i + end + 1] - prefix[i - start]
            product = nums[i] * sub_sum
            max_product = max(product, max_product)
            
        mod = pow(10, 9) + 7
        return max_product % mod
    
