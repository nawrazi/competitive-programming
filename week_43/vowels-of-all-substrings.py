# https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        size = len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        substrings = lambda n: (n * (n + 1)) // 2
        total = substrings(size)
        
        count = 0
        for idx, char in enumerate(word, 1):
            if char in vowels:
                left = substrings(idx - 1)
                right = substrings(size - idx)
                count += total - (left + right)
                
        return count
    
