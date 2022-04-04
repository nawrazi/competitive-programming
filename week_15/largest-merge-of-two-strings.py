class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merge = ''

        while len(merge) < len(word1) + len(word2):
            if word1[i:] > word2[j:]:
                merge += word1[i]
                i += 1
            else:
                merge += word2[j]
                j += 1

        return merge
