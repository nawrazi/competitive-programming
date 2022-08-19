# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for num in nums:
            while heap and heap[0][0] < num - 1:
                if heappop(heap)[1] < 3:
                    return False
                
            if not heap or heap[0][0] == num:
                heappush(heap, (num, 1))
            else:
                heappush(heap, (num, heappop(heap)[1] + 1))
                
        while heap:
            if heappop(heap)[1] < 3:
                return False
            
        return True
    
