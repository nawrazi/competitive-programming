# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        eq_attack = defaultdict(list)
        
        for a, d in properties:
            eq_attack[a].append(d)
        
        props = []
        for a, eqs in eq_attack.items():
            eqs.sort()
            props.append([a, eqs[-1]])
        
        cur_max = -inf
        weak = 0
        for a, d in sorted(props, reverse=True):
            weak += bisect_left(eq_attack[a], cur_max)
            cur_max = max(cur_max, eq_attack[a][-1])
            
        return weak
    
