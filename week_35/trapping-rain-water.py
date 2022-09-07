# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [inf for _ in range(n)]
        
        i, j = 0, n - 1
        l_max, r_max = 0, 0
        while i < n:
            water[i] = min(water[i], l_max)
            water[j] = min(water[j], r_max)
            
            l_max = max(l_max, height[i])
            r_max = max(r_max, height[j])
            
            i += 1
            j -= 1
            
        return sum([max(0, water[i] - height[i]) for i in range(n)])
    
