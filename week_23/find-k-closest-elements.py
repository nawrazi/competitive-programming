# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heappush(heap, (abs(num - x), num))
            
        return sorted([heappop(heap)[1] for _ in range(k)])
    
