# https://leetcode.com/problems/watering-plants-ii/

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alicePosition = 0
        bobPosition = len(plants) - 1
        aliceCan = capacityA
        bobCan = capacityB
        refills = 0
        while alicePosition < bobPosition:
            if aliceCan < plants[alicePosition]:
                aliceCan = capacityA
                refills += 1
            aliceCan -= plants[alicePosition]
            alicePosition += 1
            
            if bobCan < plants[bobPosition]:
                bobCan = capacityB
                refills += 1
            bobCan -= plants[bobPosition]
            bobPosition -= 1
            
        if alicePosition == bobPosition and max(bobCan, aliceCan) < plants[bobPosition]:
            refills += 1
            
        return refills
    
