# https://leetcode.com/problems/path-sum-ii/

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        allPaths = []
        
        def search(node, curSum):
            if not node.left and not node.right:
                if curSum + node.val == targetSum:
                    allPaths.append(path + [node.val])
                    
                return
            
            path.append(node.val)
            
            if node.left:
                search(node.left, curSum + node.val)
            if node.right:
                search(node.right, curSum + node.val)
                
            path.pop()
            
        if root:
            search(root, 0)
            
        return allPaths
    
