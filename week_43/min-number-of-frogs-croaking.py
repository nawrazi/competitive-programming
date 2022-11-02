# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = {'x': inf, 'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        prev = {'c': 'x', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        diff = {'c': 1, 'k': -1}
        min_frogs = 0
        cur_frogs = 0
        
        for char in croakOfFrogs:
            if char not in count or count[char] >= count[prev[char]]:
                return -1
            
            count[char] += 1
            cur_frogs += diff.get(char, 0)
            min_frogs = max(min_frogs, cur_frogs)
                
        return min_frogs if count['c'] == count['k'] else -1
    
