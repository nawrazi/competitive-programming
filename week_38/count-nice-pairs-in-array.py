# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(''.join(reversed(str(num))))
        
        def getPairs(num):
            return (num * (num - 1)) // 2
        
        mod = (10 ** 9) + 7
        diff = [num - rev(num) for num in nums]
        same = [c for c in Counter(diff).values() if c > 1]
        
        return sum(getPairs(num) for num in same) % mod
    
