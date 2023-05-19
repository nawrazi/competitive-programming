# https://leetcode.com/problems/smallest-sufficient-team/description/

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        index = {}
        for i, skill in enumerate(req_skills):
            index[skill] = i
            
        for i, skills in enumerate(people):
            mask = 0
            for skill in skills:
                mask |= (1 << index[skill])
            people[i] = mask
            
        @cache
        def getTeam(idx, mask):
            if mask == full:
                return []
            
            if idx == len(people):
                return [0] * 61
            
            pick = [idx] + getTeam(idx + 1, mask | people[idx])
            dont = getTeam(idx + 1, mask)
            return min(pick, dont, key=lambda x: len(x))
        
        full = pow(2, len(req_skills)) - 1
        return getTeam(0, 0)
    
