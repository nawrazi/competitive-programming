# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def search(node, lev):
            if not node:
                return
            
            levels[lev].append(node.val)
            
            for nex in node.children:
                search(nex, lev + 1)
                
        levels = defaultdict(list)
        search(root, 0)
        return [levels[i] for i in range(len(levels))]
    
