# https://leetcode.com/problems/split-message-based-on-limit/

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        length = len(message)
        caps = [9999, 999, 99, 9]
        while caps:
            top = caps.pop()
            size = limit - 4 - len(str(top))
            if size * top >= length:
                break
        else:
            return []
        
        caps = {10000, 1000, 100, 10}
        ans = []
        index = 1
        i = 0
        while i < length:
            if size == 0:
                return []
            part = message[i:i + size]
            ans.append(f'{part}<{index}')
            index += 1
            if index in caps:
                size -= 1
                i += 1
            i += size
            
        for i in range(len(ans)):
            ans[i] = f'{ans[i]}/{index - 1}>'
            
        return ans
    
