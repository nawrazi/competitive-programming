# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        team = skill[0] + skill[-1]
        
        for i in range(len(skill) // 2):
            chemistry += skill[i] * skill[~i]
            if skill[i] + skill[~i] != team:
                return -1
            
        return chemistry
    
