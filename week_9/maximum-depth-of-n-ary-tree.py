# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def findDepth(node, cur_depth):
            if not node: return 0

            if isLeaf(node):
                nonlocal max_depth
                max_depth = max(cur_depth,max_depth)

            for child in node.children:
                findDepth(child,cur_depth+1)

        isLeaf = lambda node : not node.children

        max_depth = 0
        findDepth(root, 1)

        return max_depth
