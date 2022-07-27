# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def earn(pos):
            if pos < 0:
                return 0
            
            if pos - 1 not in cache:
                cache[pos - 1] = earn(pos - 1)
                
            if pos - 2 not in cache:
                cache[pos - 2] = earn(pos - 2)
            
            pick = cache[pos - 2] + points[vals[pos]]
            dont_pick = cache[pos - 1]
            
            if pos > 0 and vals[pos] - vals[pos-1] > 1:
                dont_pick += points[vals[pos]]
                
            return max(pick, dont_pick)
        
        points = defaultdict(int)
        for num in nums:
            points[num] += num
            
        vals = sorted(points.keys())
        
        cache = {}
        return earn(len(vals) - 1)
    
