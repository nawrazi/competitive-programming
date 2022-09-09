# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        eq_attack = defaultdict(list)
        for a, d in sorted(properties):
            eq_attack[a].append(d)
            
        props = []
        for a, eqs in sorted(eq_attack.items()):
            props.append([a, eqs[-1]])
            
        weak, cur_max = 0, 0
        for a, d in reversed(props):
            weak += bisect_left(eq_attack[a], cur_max)
            cur_max = max(cur_max, eq_attack[a][-1])
            
        return weak
    
