# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        @cache
        def getMinDiff(day_difficulty, job, days):
            # if i have one day left, do all jobs
            if days == 1:
                return max(day_difficulty, max(jobDifficulty[job:]))
            
            day_difficulty = max(day_difficulty, jobDifficulty[job])
            
            # if i have the same number of days as jobs, do one job per day
            if days == len(jobDifficulty) - job:
                return day_difficulty + sum(jobDifficulty[job + 1:])
            
            today = getMinDiff(day_difficulty, job + 1, days)
            tomorrow = day_difficulty + getMinDiff(0, job + 1, days - 1)
            return min(today, tomorrow)
        
        return getMinDiff(0, 0, d)
    
