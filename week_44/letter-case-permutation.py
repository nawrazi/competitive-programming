# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def getPermutations(self, s, idx, current, permutations):
        if idx >= len(s):
            permutations.append(''.join(current))
            return
        
        if s[idx].isalpha():
            current.append(s[idx].upper())
            self.getPermutations(s, idx + 1, current, permutations)
            current.pop()
            
            current.append(s[idx].lower())
            self.getPermutations(s, idx + 1, current, permutations)
            current.pop()
        else:
            current.append(s[idx])
            self.getPermutations(s, idx + 1, current, permutations)
            current.pop()
    
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        current = []
        self.getPermutations(s, 0, current, permutations)
        
        return permutations
    
