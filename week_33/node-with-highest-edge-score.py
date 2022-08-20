# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = defaultdict(int)
        for i, edge in enumerate(edges):
            scores[edge] += i
            
        tuples = [(-v, k) for k, v in scores.items()]
        return sorted(tuples)[0][1]
    
