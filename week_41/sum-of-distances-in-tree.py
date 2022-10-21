# https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution:
    def getChildren(self, node, graph, parents, children):
        total_distance = 0
        for child in graph[node]:
            if child != parents[node]:
                parents[child] = node
                child_count, distance = self.getChildren(child, graph, parents, children)
                children[node] += child_count
                total_distance += distance
                
        return 1 + children[node], total_distance + children[node]
    
    def getDistances(self, node, graph, parents, children, distances, node_count):
        if node != 0:
            distances[node] = distances[parents[node]] - children[node] + node_count - 2 - children[node]
            
        for child in graph[node]:
            if child != parents[node]:
                self.getDistances(child, graph, parents, children, distances, node_count)
                
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        children = [0 for _ in range(n)]
        parents = [-1 for _ in range(n)]
        distances = [-1 for _ in range(n)]
        _, distance = self.getChildren(0, graph, parents, children)
        distances[0] = distance
        
        self.getDistances(0, graph, parents, children, distances, n)
        return distances
    
