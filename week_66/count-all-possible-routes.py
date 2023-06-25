# https://leetcode.com/problems/count-all-possible-routes/description/

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @cache
        def count(pos, tank):
            routes = int(pos == finish)
            
            for i in range(len(locations)):
                if i != pos and abs(locations[i] - locations[pos]) <= tank:
                    routes += count(i, tank - abs(locations[i] - locations[pos]))
            
            return routes % mod
        
        mod = pow(10, 9) + 7
        return count(start, fuel)
    
