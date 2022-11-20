# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution:
    def getCount(self, word):
        count = [0 for _ in range(26)]
        
        for c in word:
            count[ord(c) - ord('a')] = 1
            
        return count
    
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        targets = {}
        
        for targetWord in targetWords:
            count = tuple(self.getCount(targetWord))
            targets[count] = targets.get(count, 0) + 1
            
        conversions = 0
        for word in startWords:
            initial = self.getCount(word)
            for i in range(26):
                if initial[i] == 0:
                    initial[i] = 1
                    converted = tuple(initial)
                    if converted in targets:
                        conversions += targets[converted]
                        del targets[converted]
                    initial[i] = 0
                    
        return conversions
    
