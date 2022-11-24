# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = [[] for _ in parent]
        for node, par in enumerate(parent[1:], 1):
            graph[par].append(node)
            
        self.longest = 1
        
        def search(node):
            if not graph[node]:
                return 0
            
            longest = [0, 0]
            for child in graph[node]:
                length = 1 + search(child)
                if s[node] != s[child]:
                    longest.append(length)
                    longest.sort(reverse = True)
                    longest.pop()
                    
            self.longest = max(self.longest, sum(longest) + 1)
            return longest[0]
        
        search(0)
        return self.longest
    
