# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def search(self, prefix, target, end):
        start = 0
        while start <= end:
            mid = (start + end) // 2
            if prefix[mid] > target:
                end = mid - 1
            elif prefix[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1
    
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = []
        current = 0
        for i in range(len(nums)):
            prefix.append(nums[i] + current)
            current = prefix[-1]
            
        suffix = []
        current = 0
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(nums[i] + current)
            current = suffix[-1]
        suffix.reverse()
        
        best = inf
        for i, num in enumerate(reversed(suffix)):
            if prefix[i] == x:
                best = min(best, i + 1)
            if suffix[len(suffix) - i - 1] == x:
                best = min(best, i + 1)
                
            index = self.search(prefix, x - num, len(suffix) - i - 2)
            if index != -1:
                best = min(best, i + index + 2)
                
        return best if best != inf else -1
    
