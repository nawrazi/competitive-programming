# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_nodes = defaultdict(list)
        def search(node, level):
            if not node:
                return
            search(node.left, level + 1)
            level_nodes[level].append(node)
            search(node.right, level + 1)
        
        search(root, 0)
        for nodes in level_nodes.values():
            for i in range(1, len(nodes)):
                nodes[i-1].next = nodes[i]
        
        return root
    
