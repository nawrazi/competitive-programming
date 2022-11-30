# https://leetcode.com/problems/destroy-sequential-targets/

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mods = defaultdict(list)
        for num in nums:
            mods[num % space].append(num)
            
        best = [0, 0]
        for num in sorted(nums):
            targets = mods[num % space]
            destroyed = len(targets) - bisect_left(targets, num)
            if destroyed > best[1]:
                best = [num, destroyed]
                
        return best[0]
    
