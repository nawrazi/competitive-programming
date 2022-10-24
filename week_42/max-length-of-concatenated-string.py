# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = set()
        self.max_len = 0
        
        def concatenate(idx):
            if idx >= len(arr):
                self.max_len = max(self.max_len, len(chars))
                return
            
            can_pick = True
            for c in arr[idx]:
                if c in chars:
                    can_pick = False
                    break
                    
            # use current word
            if can_pick and len(set(arr[idx])) == len(arr[idx]):
                for c in arr[idx]:
                    chars.add(c)
                concatenate(idx + 1)
                for c in arr[idx]:
                    chars.remove(c)
                
            # don't use current word
            concatenate(idx + 1)
            
        concatenate(0)
        return self.max_len
    
