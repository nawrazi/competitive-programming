# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        score = 0
        
        for _ in range(k):
            top = -heappop(nums)
            score += top
            heappush(nums, -ceil(top / 3))
            
        return score
    
