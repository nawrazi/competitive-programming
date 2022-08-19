# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        heap = []
        for num in nums:
            while heap and heap[0][0] < num - 1:
                if heappop(heap)[1] != k:
                    return False
                
            if not heap or heap[0][0] == num or heap[0][1] == k:
                heappush(heap, (num, 1))
            else:
                heappush(heap, (num, heappop(heap)[1] + 1))
                
        while heap:
            if heappop(heap)[1] != k:
                return False
            
        return True
    
