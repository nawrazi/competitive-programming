# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda s: s.count(min(s))
        words = sorted(map(f, words))
        
        for query in map(f, queries):
            yield len(words) - bisect_right(words, query)
            
