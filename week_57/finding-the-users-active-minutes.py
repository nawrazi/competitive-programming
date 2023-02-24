# https://leetcode.com/problems/finding-the-users-active-minutes/description/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active = defaultdict(set)
        for user, time in logs:
            active[user].add(time)
            
        result = [0 for _ in range(k + 1)]
        for times in active.values():
            if len(times) <= k:
                result[len(times)] += 1
                
        return result[1:]
    
