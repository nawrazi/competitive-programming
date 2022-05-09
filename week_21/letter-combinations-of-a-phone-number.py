# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]
        
        def permutate(idx):
            chars = mapping[int(digits[idx]) - 2]
            
            if idx == len(digits) - 1:
                return chars
            
            nexts = permutate(idx + 1)
            return [char + nex for nex in nexts for char in chars]
        
        return permutate(0) if len(digits) > 0 else []
      
