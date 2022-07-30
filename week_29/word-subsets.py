# https://leetcode.com/problems/word-subsets/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letters = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for c in count:
                letters[c] = max(letters[c], count[c])
                
        supers = []
        for word in words1:
            count = Counter(word)
            sup = True
            for c in letters:
                if count[c] < letters[c]:
                    sup = False 
                    break
            if sup: supers.append(word)
                
        return supers
    
