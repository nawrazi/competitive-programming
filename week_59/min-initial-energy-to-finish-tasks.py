# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        
        def finish(energy):
            for actual, minimum in tasks:
                if energy < minimum:
                    return False
                energy -= actual
            return True
        
        left, right = 0, pow(10, 9)
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if finish(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
    
