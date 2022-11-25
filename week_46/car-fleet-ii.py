# https://leetcode.com/problems/car-fleet-ii/

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        time = lambda car1, car2: (car2[0] - car1[0]) / (car1[1] - car2[1])
        result = [-1 for _ in cars]
        stack = []
        
        for idx, car in enumerate(reversed(cars)):
            current = [*car, inf]
            
            while stack and (car[1] <= stack[-1][1] or time(car, stack[-1]) >= stack[-1][2]):
                stack.pop()
                
            if stack:
                result[~idx] = current[2] = time(car, stack[-1])
                
            stack.append(current)
            
        return result
    
