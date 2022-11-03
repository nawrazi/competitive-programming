# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        length = 0
        centered = False
        for word, count in counts.items():
            if word[::-1] not in counts:
                continue
                
            if word != word[::-1]:
                length += min(count, counts[word[::-1]])
                continue
                
            if count % 2 == 1:
                if centered:
                    length += count - 1
                else:
                    length += count
                    centered = True
            else:
                length += count
                
        return length * 2
    
