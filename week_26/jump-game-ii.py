# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])
        seen = set()
        
        while q:
            cur_idx, cur_lvl = q.popleft()
            
            if cur_idx == len(nums) - 1:
                return cur_lvl
            
            for i in range(1, nums[cur_idx] + 1):
                nex_idx = cur_idx + i
                if nex_idx not in seen:
                    q.append((nex_idx, cur_lvl + 1))
                    seen.add(nex_idx)
                    
