# https://leetcode.com/problems/utf-8-validation/

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def getFirst(num):
            mask = 2 ** 7
            count = 1
            for _ in range(8):
                if num & mask == 0:
                    break
                mask >>= 1
                count += 1
                
            return count
        
        on = False
        length = 0
        for num in data:
            first = getFirst(num)
            if on and first != 2:
                return False
            
            if first == 2:
                length -= 1
                if not on or length < 0:
                    return False
                if length == 0:
                    on = False
                
            elif first == 1:
                continue
                
            elif first > 5:
                return False
            
            else:
                on = True
                length = first - 2
                
        return not on
    
