# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0
        
        def search(node, goLeft, path):
            nonlocal longest
            if not node:
                return
            
            longest = max(longest, path)
            if goLeft:
                search(node.left, False, path + 1)
                search(node.right, True, 1)
            else:
                search(node.left, False, 1)
                search(node.right, True, path + 1)
                
        search(root, True, 0)
        search(root, False, 0)
        return longest
    
