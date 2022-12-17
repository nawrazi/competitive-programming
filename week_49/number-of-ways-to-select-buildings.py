# https://leetcode.com/problems/number-of-ways-to-select-buildings/description/

class Solution:
    def numberOfWays(self, s: str) -> int:
        suffix = {'0': [], '1': []}
        prev_zeros, prev_ones = 0, 0
        for c in reversed(s):
            suffix['1'].append(prev_zeros)
            suffix['0'].append(prev_ones)
            
            if c == '0':
                prev_zeros += 1
            else:
                prev_ones += 1
                
        ways = 0
        prefix = {'0': 0, '1': 0}
        for i, c in enumerate(s):
            ways += prefix[c] * suffix[c][~i]
            
            if c == '0':
                prefix['1'] += 1
            else:
                prefix['0'] += 1
                
        return ways
    
