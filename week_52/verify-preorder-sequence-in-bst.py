# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        root = Node(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = Node(val)

            if node.val < stack[-1].val:
                stack[-1].left = node

            else:
                while stack and node.val > stack[-1].val:
                    last = stack.pop()
                last.right = node

            stack.append(node)

        self.last = -1

        def verify(node):
            if not node:
                return True

            if not verify(node.left) or node.val < self.last:
                return False

            self.last = node.val
            
            if not verify(node.right):
                return False

            return True

        return verify(root)
