# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ordered = []
        counts = []
        
        for num in reversed(nums):
            pos = bisect_left(ordered, num)
            counts.append(pos)
            ordered.insert(pos, num)
            
        return counts[::-1]
    
