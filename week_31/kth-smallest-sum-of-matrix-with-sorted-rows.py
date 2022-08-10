# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        first_chosen = [0 for _ in range(m)]
        first_sum = sum([mat[i][idx] for i, idx in enumerate(first_chosen)])
        heap = [(first_sum, first_chosen)]
        seen = {tuple(first_chosen)}
        
        for _ in range(k):
            cur_sum, cur_chosen = heappop(heap)
            
            for i in range(m):
                cur_chosen[i] += 1
                
                if tuple(cur_chosen) not in seen and cur_chosen[i] < n:
                    next_sum = sum([mat[i][idx] for i, idx in enumerate(cur_chosen)])
                    heappush(heap, (next_sum, cur_chosen[:]))
                    seen.add(tuple(cur_chosen))
                    
                cur_chosen[i] -= 1
                
        return cur_sum
    
