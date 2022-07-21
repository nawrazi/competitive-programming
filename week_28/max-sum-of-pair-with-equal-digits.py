# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = defaultdict(list)
        for num in nums:
            dig_sum = 0
            cur_num = num
            while cur_num > 0:
                dig_sum += cur_num % 10
                cur_num //= 10
                
            if len(digits[dig_sum]) >= 2:
                cur_min = min(digits[dig_sum])
                digits[dig_sum].remove(cur_min)
                num = max(num, cur_min)
                
            digits[dig_sum].append(num)
            
        max_sum = -1
        for vals in digits.values():
            if len(vals) == 2:
                max_sum = max(max_sum, sum(vals))
            
        return max_sum
    
