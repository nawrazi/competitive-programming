# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = [-inf, -inf, -inf]
        for num in set(nums):
            top3.append(num)
            top3.sort(reverse=True) # O(1)
            top3.pop()
            
        while top3[-1] == -inf:
            top3.pop()
            
        return top3[2] if len(top3) == 3 else top3[0]
    
