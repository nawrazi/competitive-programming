# https://leetcode.com/problems/crawler-log-folder/description/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log[:-1] == '..':
                depth = max(0, depth - 1)
            elif log[:-1] != '.':
                depth += 1
                
        return depth
    
