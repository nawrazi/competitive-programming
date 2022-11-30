# https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        size = len(costs)
        heap = []
        left, right = 0, size - 1
        while candidates and left <= right:
            heappush(heap, (costs[left], left, True))
            if left != right:
                heappush(heap, (costs[right], right, False))
            left += 1
            right -= 1
            candidates -= 1
        
        total = 0
        for _ in range(k):
            cost, _, isLeft = heappop(heap)
            total += cost
            if left > right:
                continue
            if isLeft:
                heappush(heap, (costs[left], left, True))
                left += 1
            else:
                heappush(heap, (costs[right], right, False))
                right -= 1
                    
        return total
    
