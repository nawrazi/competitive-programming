# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        axis = [0 for _ in range(2 * pow(10, 5) + 1)]
        max_fruits = 0
        
        for pos, amount in fruits:
            axis[pos] = amount
            
        for pos in range(startPos + 1, len(axis)):
            axis[pos] += axis[pos - 1]
            
        for pos in range(startPos - 1, -1, -1):
            axis[pos] += axis[pos + 1]
            
        for pos in range(startPos, len(axis)):
            if pos - startPos > k:
                break
            right = axis[pos]
            if 2 * (pos - startPos) <= k:
                left = axis[max(startPos - (k - (2 * (pos - startPos))), 0)]
            else:
                left = 0
            max_fruits = max(max_fruits, left + right - axis[startPos])
            
        for pos in range(startPos, -1, -1):
            if startPos - pos > k:
                break
            left = axis[pos]
            if 2 * (startPos - pos) <= k:
                right = axis[min(startPos + (k - (2 * (startPos - pos))), len(axis) - 1)]
            else:
                right = 0
            max_fruits = max(max_fruits, left + right - axis[startPos])
            
        return max_fruits
    
