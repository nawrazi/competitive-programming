# https://leetcode.com/problems/count-good-meals/

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = (10 ** 9) + 7
        powers = [pow(2, i) for i in range(22)]
        diffs = defaultdict(int)
        good_meals = 0
        
        for food in deliciousness:
            if food in diffs:
                good_meals += diffs[food]
            for power in powers:
                diffs[power - food] += 1
                
        return good_meals % mod
    
