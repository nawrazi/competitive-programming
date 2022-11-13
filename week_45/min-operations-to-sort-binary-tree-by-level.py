# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        def search(node, level):
            if not node:
                return
            levels[level].append(node.val)
            search(node.left, level + 1)
            search(node.right, level + 1)
            
        search(root, 0)
        
        current = defaultdict(dict)
        mapping = defaultdict(dict)
        for level in range(len(levels)):
            for pos, num in enumerate(levels[level]):
                current[level][num] = pos
                mapping[level][pos] = num
            levels[level].sort()
            
        swaps = 0
        for level in range(len(levels)):
            for app_pos, num in enumerate(levels[level]):
                cur_pos = current[level][num]
                if cur_pos != app_pos:
                    swaps += 1
                    tbs = mapping[level][app_pos]
                    current[level][num] = app_pos
                    current[level][tbs] = cur_pos
                    mapping[level][app_pos] = num
                    mapping[level][cur_pos] = tbs
                    
        return swaps
    
