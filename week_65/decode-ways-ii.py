# https://leetcode.com/problems/decode-ways-ii/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def getWays(idx):
            if idx >= len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s) - 1:
                return 1 if s[idx] != '*' else 9
            
            ways = 0
            if s[idx] == '*':
                for num1 in range(1, 10):
                    ways += getWays(idx + 1)
                    
                    if s[idx + 1] == '*':
                        for num2 in range(1, 10):
                            if (10 * num1) + num2 <= 26:
                                ways += getWays(idx + 2)
                    
                    elif (10 * num1) + int(s[idx + 1]) <= 26:
                        ways += getWays(idx + 2)
            
            elif s[idx + 1] == '*':
                ways += getWays(idx + 1)
                for num2 in range(1, 10):
                    if (10 * int(s[idx])) + num2 <= 26:
                        ways += getWays(idx + 2)
            
            else:
                ways += getWays(idx + 1)
                if (10 * int(s[idx])) + int(s[idx + 1]) <= 26:
                    ways += getWays(idx + 2)
            
            return ways % mod
        
        mod = pow(10, 9) + 7
        return getWays(0)
    
