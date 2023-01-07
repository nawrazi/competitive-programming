# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        
        left, right = 0, pow(10, 5)
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) <= finalSum:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
                
        result = [2 * num for num in range(1, best)]
        result.append(finalSum - (best * (best - 1)))
        
        return result
    
