# https://leetcode.com/problems/largest-component-size-by-common-factor/

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
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
            n, d = num, 2
            
            while d * d <= n:
                while n % d == 0:
                    union(num, d)
                    n //= d
                d += 1
            if n > 1:
                union(num, n)
        
        for num in nums:
            factorize(num)
        
        groups = Counter(find(num) for num in nums)
        return max(groups.values())
    
