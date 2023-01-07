# https://leetcode.com/problems/design-an-atm-machine/description/

class ATM:

    def __init__(self):
        self.cash = [0 for _ in range(5)]
        self.cash_map = [20, 50, 100, 200, 500]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.cash[i] += count
            
    def withdraw(self, amount: int) -> List[int]:
        if not any(self.cash):
            return [-1]
        
        note = 4
        while self.cash[note] == 0:
            note -= 1
            
        backup = self.cash[:]
        money = [0 for _ in range(5)]
        
        while amount > 0 and note >= 0:
            if amount >= self.cash_map[note]:
                ideal = amount // self.cash_map[note]
                real = min(ideal, self.cash[note])
                money[note] += real
                self.cash[note] -= real
                amount -= real * self.cash_map[note]
            note -= 1
            
        if amount > 0:
            self.cash = backup[:]
            return [-1]
        
        return money
    
