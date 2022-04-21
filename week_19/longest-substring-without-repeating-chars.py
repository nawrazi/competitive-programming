# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0

        i, j = 0, 0
        while i < len(s):
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
                
            max_length = max(max_length, j - i)
            seen.remove(s[i])
            i += 1

        return max_length
