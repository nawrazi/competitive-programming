# https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/

class Solution:
    def balancedString(self, s: str) -> int:
        counts = Counter(s)
        min_length = inf
        left = 0
        
        if set(counts.values()) == {len(s) // 4}:
            return 0
        
        for right in range(len(s)):
            counts[s[right]] -= 1
            
            while max(counts.values()) <= len(s) // 4:
                min_length = min(min_length, right - left + 1)
                counts[s[left]] += 1
                left += 1
                
        return min_length
    
