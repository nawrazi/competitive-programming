# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def canChoose(diff):
            last = price[0]
            taken = 1
            for candy in price:
                if candy - last >= diff:
                    last = candy
                    taken += 1
                    
            return taken >= k
        
        price.sort()
        low, high = 0, max(price) - min(price)
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if canChoose(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return best
    
