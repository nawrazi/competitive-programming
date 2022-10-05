# https://leetcode.com/problems/clone-graph/

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {None: None}
        
        def clone(node):
            if node not in cloned:
                cloned[node] = Node(node.val)
                for ngh in node.neighbors:
                    cloned[node].neighbors.append(clone(ngh))
                    
            return cloned[node]
        
        return clone(node)
    
