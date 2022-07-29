# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def search(node):
            if not node:
                return
            
            search(node.left)
            nodes.append(node.val)
            search(node.right)
            
        nodes = []
        search(root1)
        search(root2)
        
        return sorted(nodes)
    
