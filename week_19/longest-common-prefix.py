# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            cur_letter = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != cur_letter:
                    return prefix

            prefix += cur_letter

        return prefix
