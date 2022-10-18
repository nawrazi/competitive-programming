# https://leetcode.com/problems/watering-plants/

class Solution:
    def getPlantsWatered(self, plants, capacity, offset):
        left, right = 0, len(plants) - 1
        best = len(plants)
        while left <= right:
            mid = (left + right) // 2
            if capacity > plants[mid] - offset:
                left = mid + 1
                best = left
            elif capacity < plants[mid] - offset:
                right = mid - 1
            else:
                return mid + 1
            
        return best
    
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        prefix = 0
        for i in range(len(plants)):
            prefix += plants[i]
            plants[i] = prefix
            
        steps = 0
        offset = 0
        while offset < plants[-1]:
            plantsWatered = self.getPlantsWatered(plants, capacity, offset)
            steps += plantsWatered * 2
            offset = plants[plantsWatered - 1]
            
        return steps - plantsWatered
    
