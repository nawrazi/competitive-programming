# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def search(root):
            start, end = 0, root
            
            while start <= end:
                mid = (start + end) // 2
                val = (mid ** 2) + (root ** 2)
                
                if val < c:
                    start = mid + 1
                elif val > c:
                    end = mid - 1
                else:
                    return True
                
        for i in range(floor(sqrt(c)) + 1):
            if search(i):
                return True
            
        return False
    
