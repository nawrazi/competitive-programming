# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = set()
        
        def backtrack(cur):
            if len(cur) == n:
                nums.add(int(cur))
                return
            
            if 0 <= int(cur[-1]) + k < 10:
                backtrack(cur + str(int(cur[-1]) + k))
                
            if 0 <= int(cur[-1]) - k < 10:
                backtrack(cur + str(int(cur[-1]) - k))
                
        for i in range(1, 10):
            backtrack(str(i))
            
        return nums
    
