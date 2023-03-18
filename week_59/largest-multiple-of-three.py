# https://leetcode.com/problems/largest-multiple-of-three/description/

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        mods = [[], [], []]
        total = sum(digits)
        
        for digit in digits:
            mods[digit % 3].append(digit)
            
        for mod in mods:
            mod.sort(reverse=True)
            
        if total % 3 == 1:
            if mods[1]:
                mods[1].pop()
            elif len(mods[2]) >= 2:
                mods[2].pop()
                mods[2].pop()
                
        if total % 3 == 2:
            if mods[2]:
                mods[2].pop()
            elif len(mods[1]) >= 2:
                mods[1].pop()
                mods[1].pop()
                
        res = ''.join(map(str, sorted(chain(*mods), reverse=True)))
        return str(int(res)) if res else ''
    
