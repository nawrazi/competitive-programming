# https://leetcode.com/problems/binary-tree-cameras/

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def install(node):
            if not node:
                return 0, 1
            
            camerasLeft, nearestLeft = install(node.left)
            camerasRight, nearestRight = install(node.right)
            
            cameras = camerasLeft + camerasRight
            if nearestLeft > 1 or nearestRight > 1:
                return cameras + 1, 0
            else:
                return cameras, min(nearestLeft, nearestRight) + 1
            
        cameras, nearest = install(root)
        return cameras if nearest <= 1 else cameras + 1
    
