# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        counts = [Counter() for _ in words[0]]
        for i in range(len(words[0])):
            for word in words:
                counts[i][word[i]] += 1
                
        @cache
        def count(w, t):
            if t >= len(target):
                return 1
            if w >= len(counts):
                return 0
            
            ways = count(w + 1, t)
            if target[t] in counts[w]:
                ways += counts[w][target[t]] * count(w + 1, t + 1)
                
            return ways % mod
        
        mod = pow(10, 9) + 7
        return count(0, 0)
    
