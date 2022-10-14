# https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur, mode = [inf, inf], [-inf, []]
        
        def iot(node):
            if not node:
                return
            
            iot(node.left)
            
            if node.val == cur[0]:
                cur[1] += 1
            else:
                cur[0], cur[1] = node.val, 1
                
            if cur[1] > mode[0]:
                mode[0], mode[1] = cur[1], [node.val]
            elif cur[1] == mode[0]:
                mode[1].append(node.val)
                
            iot(node.right)
            
        iot(root)
        return mode[1]
    
