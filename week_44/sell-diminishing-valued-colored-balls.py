# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:    
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = (10 ** 9) + 7
        counts = Counter(inventory)
        inventory = sorted(list(counts.keys()) + [0], reverse=True)
        getSum = lambda num: (num * (num + 1)) // 2
        
        total = 0
        i = 0
        width = counts[inventory[0]]
        while orders > 0 and i < len(inventory) - 1:
            if orders >= width * (inventory[i] - inventory[i + 1]):
                value = width * (getSum(inventory[i]) - getSum(inventory[i + 1]))
                orders -= width * (inventory[i] - inventory[i + 1])
            else:
                div = orders // width
                main = width * (getSum(inventory[i]) - getSum(inventory[i] - div))
                extra = (orders % width) * (inventory[i] - div)
                value = main + extra
                orders = 0
                
            total += value
            i += 1
            width += counts[inventory[i]]
            
        return total % mod
    
