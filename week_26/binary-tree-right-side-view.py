# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def search(node, level):
            if not node: 
                return
            
            search(node.left, level+1)
            levels[level].append(node.val)
            search(node.right, level+1)
            
        levels = defaultdict(list)
        search(root, 0)
        
        return [levels[i][-1] for i in range(len(levels))]
        
