# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def getMinSteps(on_screen, on_clip):
            if on_screen == n:
                return 0
            if on_screen > n:
                return inf
            
            copy_paste = getMinSteps(on_screen * 2, on_screen) + 2
            just_paste = getMinSteps(on_screen + on_clip, on_clip) + 1
            
            return min(copy_paste, just_paste)
        
        return getMinSteps(2, 1) + 2 if n != 1 else 0
    
