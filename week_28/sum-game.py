# https://leetcode.com/problems/sum-game/

class Solution:
    def sumGame(self, num: str) -> bool:
        sums, quests = [0, 0], [0, 0]
        half = len(num) // 2
        for i, n in enumerate(num):
            if n == '?':
                quests[i // half] += 1
            else:
                sums[i // half] += int(n)
                
        if sums[1] > sums[0]:
            sums.reverse()
            quests.reverse()
            
        turn = 1
        while quests[0] > 0:
            sums[0] += turn * 9
            turn ^= 1
            quests[0] -= 1
        
        while quests[1] > 0:
            if sums[0] == sums[1]:
                return True
            sums[1] += (turn ^ 1) * 9
            turn ^= 1
            quests[1] -= 1
            
        return sums[0] != sums[1]
    
