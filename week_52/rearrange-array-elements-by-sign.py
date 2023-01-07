# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
                
        res = []
        while pos:
            res.append(neg.pop())
            res.append(pos.pop())
            
        return res[::-1]
    
