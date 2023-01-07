# https://leetcode.com/problems/random-pick-with-weight/description/

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))
        
    def pickIndex(self) -> int:
        value = random.uniform(0, self.prefix[-1])
        left, right = 0, len(self.prefix) - 1
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.prefix[mid] > value:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
    
