# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix = [0]
        for bean in beans:
            prefix.append(prefix[-1] + bean)
            
        min_beans = inf
        for i in range(len(beans)):
            left = prefix[i]
            right = (prefix[-1] - prefix[i+1]) - (beans[i] * (len(beans) - i - 1))
            min_beans = min(min_beans, left + right)
            
        return min_beans
    
