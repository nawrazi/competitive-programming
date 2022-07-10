# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float(inf), float(inf)
        for num in nums:
            if num < i:
                i = num
            elif num < j and num > i:
                j = num
            elif num > j:
                return True
            
        return False
    
