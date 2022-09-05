# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def search(node, col, row):
            if not node:
                return
            
            cols[col].append((row, node.val))
            
            search(node.left, col - 1, row + 1)
            search(node.right, col + 1, row + 1)
            
        cols = defaultdict(list)
        search(root, 0, 0)
        
        pairs = sorted([(i, sorted(c)) for i, c in cols.items()])
        return [[v for _, v in c] for _, c in pairs]
    
