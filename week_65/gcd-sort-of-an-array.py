# https://leetcode.com/problems/gcd-sort-of-an-array/description/

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
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
        
        for num in nums:
            factorize(num)
        
        groups = defaultdict(list)
        for num in nums:
            groups[find(num)].append(num)
        
        for parent in groups:
            groups[parent].sort(reverse=True)
        
        result = []
        for num in nums:
            result.append(groups[find(num)].pop())
        
        for i in range(1, len(result)):
            if result[i] < result[i - 1]:
                return False
        
        return True
    
