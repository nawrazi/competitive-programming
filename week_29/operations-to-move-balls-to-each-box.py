# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0 for _ in range(len(boxes))]
        places = set([i for i, ball in enumerate(boxes) if ball == '1'])
        
        for i in range(len(boxes)):
            for place in places:
                ans[i] += abs(place - i)
                
        return ans
    
