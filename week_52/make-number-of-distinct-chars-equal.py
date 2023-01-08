# https://leetcode.com/problems/make-number-of-distinct-characters-equal/description/

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        
        for letter1 in list(counter1.keys()):
            for letter2 in list(counter2.keys()):
                counter1[letter1] -= 1
                if counter1[letter1] == 0:
                    del counter1[letter1]
                counter2[letter1] += 1
                
                counter2[letter2] -= 1
                if counter2[letter2] == 0:
                    del counter2[letter2]
                counter1[letter2] += 1
                
                if len(counter1) == len(counter2):
                    return True
                
                counter2[letter1] -= 1
                if counter2[letter1] == 0:
                    del counter2[letter1]
                counter1[letter1] += 1
                
                counter1[letter2] -= 1
                if counter1[letter2] == 0:
                    del counter1[letter2]
                counter2[letter2] += 1
                
        return False
    
