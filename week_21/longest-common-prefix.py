# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i in range(199):
            if i >= len(strs[0]):
                return ''.join(prefix)
            
            cur_letter = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != cur_letter:
                    return ''.join(prefix)
                
            prefix.append(cur_letter)
