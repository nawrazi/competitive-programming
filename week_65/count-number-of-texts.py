# https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        possible = {'7': 4, '9': 4}
        mod = pow(10, 9) + 7
        dp = [0 for _ in range(len(pressedKeys))] + [1]
        
        for idx in range(len(dp) - 2, -1, -1):
            for i in range(idx, idx + possible.get(pressedKeys[idx], 3)):
                if i >= len(pressedKeys) or pressedKeys[i] != pressedKeys[idx]:
                    break
                dp[idx] += dp[i + 1]
        
        return dp[0] % mod
    
