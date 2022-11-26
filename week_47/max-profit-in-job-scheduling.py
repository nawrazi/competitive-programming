# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def findEarliest(time):
            left, right = 0, jobs - 1
            best = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if starts[mid][0] >= time:
                    best = mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return best
        
        @cache
        def getProfit(job):
            if not -1 < job < jobs:
                return 0
            
            next_job = findEarliest(ends[job])
            return max(getProfit(job + 1), profits[job] + getProfit(next_job))
        
        jobs = len(startTime)
        starts = sorted((start, job) for job, start in enumerate(startTime))
        ends = []
        profits = []
        
        for _, job in starts:
            ends.append(endTime[job])
            profits.append(profit[job])
            
        return getProfit(0)
    
