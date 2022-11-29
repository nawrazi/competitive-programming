# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def search(node):
            if node:
                search(node.left)
                nodes.append(node.val)
                search(node.right)
        
        def bisect(target):
            left, right = 0, len(nodes) - 1
            low, high = -1, -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nodes[mid] <= target:
                    left = mid + 1
                    low = nodes[mid]
                if nodes[mid] >= target:
                    right = mid - 1
                    high = nodes[mid]
            
            return [low, high]
        
        nodes = []
        search(root)
        return [bisect(query) for query in queries]
    
