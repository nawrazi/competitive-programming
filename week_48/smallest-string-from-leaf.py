# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        current = []
        self.smallest = chr(ord('z') + 1)
        
        def search(node):
            current.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                self.smallest = min(''.join(current[::-1]), self.smallest)
            else:
                if node.left:
                    search(node.left)
                if node.right:
                    search(node.right)
            current.pop()
            
        search(root)
        return self.smallest
    
