# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/

class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def count(pickup, delivery):
            if pickup == delivery == 0:
                return 1
            
            options = 0
            if pickup:
                options += pickup * count(pickup - 1, delivery + 1)
                
            if delivery:
                options += delivery * count(pickup, delivery - 1)
                
            return options % mod
        
        mod = pow(10, 9) + 7
        return count(n, 0)
    
