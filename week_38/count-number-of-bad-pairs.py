# https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        def getPairs(num):
            return (num * (num - 1)) // 2
        
        diff = [n - i for i, n in enumerate(nums)]
        same = [c for c in Counter(diff).values() if c > 1]
        
        total = getPairs(len(nums))
        good = sum(getPairs(n) for n in same)
        
        return total - good
    
