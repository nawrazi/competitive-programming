# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        previous = defaultdict(lambda: Node)
        
        def search(node, level):
            if not node:
                return
            
            previous[level].next = node
            previous[level] = node
            
            search(node.left, level + 1)
            search(node.right, level + 1)
            
        search(root, 0)
        return root
    
