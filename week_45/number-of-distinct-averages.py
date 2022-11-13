# https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        queue = deque(sorted(nums))
        averages = set()
        
        while queue:
            average = (queue.pop() + queue.popleft()) / 2
            averages.add(average)
            
        return len(averages)
    
