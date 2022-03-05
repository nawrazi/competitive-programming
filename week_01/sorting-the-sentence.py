# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sent_list = [None for _ in range(len(words))]
        for word in words:
            index = int(word[-1]) - 1
            sent_list[index] = word[:-1]

        return ' '.join(sent_list)
