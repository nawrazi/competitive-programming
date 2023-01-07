# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def match(str1, str2):
            idx1, idx2 = 0, 0
            while idx1 < len(str1) and idx2 < len(str2):
                if str1[idx1] == str2[idx2]:
                    idx1 += 1
                idx2 += 1
                
            return idx1 == len(str1)
        
        longest = -1
        for idx1, str1 in enumerate(strs):
            for idx2, str2 in enumerate(strs):
                if idx1 != idx2 and match(str1, str2):
                    break
            else:
                longest = max(longest, len(str1))
                
        return longest
    
