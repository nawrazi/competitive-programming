# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        pos = defaultdict(set)
        count = Counter(secret)
        for i, c in enumerate(secret):
            pos[c].add(i)
            
        bulls = set()
        for i, c in enumerate(guess):
            if c in pos and count[c] and i in pos[c]:
                bulls.add(i)
                count[c] -= 1
                
        cows = 0
        for i, c in enumerate(guess):
            if c in pos and count[c] and i not in bulls:
                cows += 1
                count[c] -= 1
                
        return f'{len(bulls)}A{cows}B'
    
