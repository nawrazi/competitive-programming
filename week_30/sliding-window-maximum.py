# https://leetcode.com/problems/sliding-window-maximum/

from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList()
        sl.update(nums[:k])
        maxes = []
        
        i, j = 0, k - 1
        while j < len(nums) - 1:
            maxes.append(sl[-1])
            sl.discard(nums[i])
            sl.add(nums[j + 1])
            i += 1
            j += 1
            
        maxes.append(max(nums[i:j + 1]))
        return maxes
    
