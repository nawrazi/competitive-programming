# https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        parents = [-1 for _ in nums]
        segments = [0 for _ in nums]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            segments[parent1] += segments[parent2]
            parents[parent1] += parents[parent2]
            parents[parent2] = parent1
            
        result = [0]
        for idx in removeQueries[1:][::-1]:
            segments[idx] = nums[idx]
            if idx > 0 and segments[idx - 1] != 0:
                union(idx, idx - 1)
            if idx < len(nums) - 1 and segments[idx + 1] != 0:
                union(idx, idx + 1)
            result.append(max(result[-1], segments[find(idx)]))
            
        return result[::-1]
    
