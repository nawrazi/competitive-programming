# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        
        for num in preorder[1:]:
            node = TreeNode(num)
            
            if node.val < stack[-1].val:
                stack[-1].left = node
                
            else:
                while stack and node.val > stack[-1].val:
                    last = stack.pop()
                last.right = node
                
            stack.append(node)
            
        return root
    
