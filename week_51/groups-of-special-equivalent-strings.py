# https://leetcode.com/problems/groups-of-special-equivalent-strings/description/

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = Counter()
        
        for word in words:
            counts = [[0] * 26 for _ in range(2)]
            for i, char in enumerate(word):
                counts[i % 2][ord(char) - ord('a')] += 1
                
            groups[tuple(map(tuple, counts))] += 1
            
        return len(groups)
    
