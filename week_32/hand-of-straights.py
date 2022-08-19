# https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        heap = []
        for num in hand:
            while heap and heap[0][0] < num - 1:
                if heappop(heap)[1] != groupSize:
                    return False
                
            if not heap or heap[0][0] == num or heap[0][1] == groupSize:
                heappush(heap, (num, 1))
            else:
                heappush(heap, (num, heappop(heap)[1] + 1))
                
        while heap:
            if heappop(heap)[1] != groupSize:
                return False
            
        return True
    
