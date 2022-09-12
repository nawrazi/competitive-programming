# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        options = deque(sorted(tokens))
        score = 0
        last_buy = False
        
        while options:
            if power >= options[0]:
                power -= options.popleft()
                score += 1
                last_buy = False
            elif score > 0:
                power += options.pop()
                score -= 1
                last_buy = True
            else:
                break
                
        return score + 1 if last_buy else score
    
