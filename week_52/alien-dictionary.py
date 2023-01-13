# https://practice.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self,dict, N, K):
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for i in range(N - 1):
            word1, word2 = dict[i], dict[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indeg[word2[j]] += 1
                    break
                
        queue = deque()
        order = []
        
        for i in range(K):
            char = chr(ord('a') + i)
            if indeg[char] == 0:
                queue.append(char)
                
        while queue:
            char = queue.popleft()
            order.append(char)
            
            for ngh in graph[char]:
                indeg[ngh] -= 1
                if indeg[ngh] == 0:
                    queue.append(ngh)
                    
        return ''.join(order)
    
