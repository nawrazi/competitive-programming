# https://leetcode.com/problems/validate-binary-tree-nodes/description/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [-1 for _ in range(n)]
        hasParent = [False for _ in range(n)]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
                return True
            
        for node, (left, right) in enumerate(zip(leftChild, rightChild)):
            if (left != -1 and hasParent[left]) or (right != -1 and hasParent[right]):
                return False
            if (left != -1 and not union(node, left)) or (right != -1 and not union(node, right)):
                return False
            if left != -1:
                hasParent[left] = True
            if right != -1:
                hasParent[right] = True
                
        return sum(1 for p in parents if p < 0) == 1
    
