# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [[0, 0] for _ in range(n + 1)]
        for a, b in trust:
            degree[a][0] += 1
            degree[b][1] += 1
            
        for p, (o, i) in enumerate(degree[1:], 1):
            if i == n - 1 and o == 0:
                return p
            
        return -1
    
