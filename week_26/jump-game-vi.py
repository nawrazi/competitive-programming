class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        
        for cur in range(1, len(nums)):
            while cur - heap[0][1] > k:
                heappop(heap)
            heappush(heap, (heap[0][0] - nums[cur], cur))
            
        while heap[0][1] < len(nums) - 1:
            heappop(heap)
            
        return -heappop(heap)[0]
      
