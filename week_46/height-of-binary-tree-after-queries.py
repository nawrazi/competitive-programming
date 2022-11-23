# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = {}
        height = {}
        level_max = defaultdict(lambda: [-inf, -inf])
        
        def search(node, level):
            if node is None:
                return 0
            
            left = search(node.left, level + 1)
            right = search(node.right, level + 1)
            cur_height = 1 + max(left, right)
            
            height[node.val] = cur_height
            levels[node.val] = level
            level_max[level].append(cur_height)
            level_max[level].sort(reverse = True)
            level_max[level].pop()
            
            return cur_height
        
        original = search(root, 0)
        ans = []
        
        for node in queries:
            level = levels[node]
            
            if height[node] == level_max[level][0]:
                if level_max[level][1] != -inf:
                    ans.append(level_max[level][1] + level - 1)
                else:
                    ans.append(original - height[node] - 1)
            else:
                ans.append(original - 1)
        
        return ans
    
