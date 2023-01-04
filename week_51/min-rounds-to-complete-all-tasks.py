# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        rounds = 0
        
        for count in counts.values():
            if count == 1:
                return -1
            rounds += (count // 3) + int(count % 3 != 0)
            
        return rounds
    
