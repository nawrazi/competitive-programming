# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(num):
            path.append(num)
            seen.add(num)
            
            for nex in graph[num]:
                if nex not in seen:
                    dfs(nex)
                    
            seen.remove(num)
            if len(path) == len(nums):
                ans.append(path.copy())
            path.pop()
            
        graph = defaultdict(list)
        
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    graph[num1].append(num2)
                    
        ans = []
        path = []
        seen = set()
        
        for num in nums:
            dfs(num)
            
        return ans
 
