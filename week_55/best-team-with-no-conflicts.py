# https://leetcode.com/problems/best-team-with-no-conflicts/description/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        stats = [(score, age) for age, score in sorted(zip(ages, scores))]
        
        @cache
        def getScore(idx, top):
            if idx >= len(stats):
                return 0
            
            score = getScore(idx + 1, top)
            if stats[idx][0] >= top:
                score = max(score, stats[idx][0] + getScore(idx + 1, stats[idx][0]))
                
            return score
        
        score = getScore(0, 0)
        getScore.cache_clear()
        return score
    
