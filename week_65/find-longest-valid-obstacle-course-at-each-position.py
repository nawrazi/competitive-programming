# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = []
        for num in obstacles:
            pos = bisect_right(dp, num)
            
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
            
            yield pos + 1
        
