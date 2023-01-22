# https://leetcode.com/problems/count-the-hidden-sequences/description/

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = list(accumulate(differences, initial=0))
        return max(upper - lower - (max(prefix) - min(prefix)) + 1, 0)
    
