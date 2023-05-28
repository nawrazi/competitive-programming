# https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        parents = [-1 for _ in range(max(nums) + 1)]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
        
        def factorize(num):
            n = num
            d = 2
            
            while d * d <= n:
                while n % d == 0:
                    union(num, d)
                    n //= d
                d += 1
            if n > 1:
                union(num, n)
            
        if set(nums) == {1} and len(nums) > 1:
            return False
        
        for num in nums:
            factorize(num)
        
        return all(find(num) == find(nums[0]) for num in nums)
    
