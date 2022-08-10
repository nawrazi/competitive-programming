# https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def search(node, target):
            if not node:
                return False
            
            result = False
            if node.val == target.val:
                if not target.next:
                    return True
                result = search(node.left, target.next) or search(node.right, target.next)
                
            return result or search(node.left, head) or search(node.right, head)
                
        return search(root, head)
    
