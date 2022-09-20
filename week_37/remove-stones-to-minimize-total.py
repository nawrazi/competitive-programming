# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-p for p in piles]
        heapify(piles)
        while k:
            top = -heappop(piles)
            diff = top // 2
            total -= diff
            heappush(piles, -top + diff)
            k -= 1
            
        return total
    
