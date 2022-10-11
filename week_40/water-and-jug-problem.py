# https://leetcode.com/problems/water-and-jug-problem/

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def getGcd(a, b):
            if a == 0:
                return b
            return getGcd(b % a, a)
        
        gcd = getGcd(jug1Capacity, jug2Capacity)
        for i in range(gcd, jug1Capacity + jug2Capacity + 1, gcd):
            if i == targetCapacity:
                return True
            
        return False
    
