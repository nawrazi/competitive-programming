# https://leetcode.com/problems/profitable-schemes/description/

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def countSchemes(crime, people, money):
            if crime == len(group):
                return int(money == minProfit)
            
            schemes = countSchemes(crime + 1, people, money)
            if people + group[crime] <= n:
                schemes += countSchemes(crime + 1, people + group[crime], min(minProfit, money + profit[crime]))
                
            return schemes % mod
        
        mod = pow(10, 9) + 7
        return countSchemes(0, 0, 0)
    
