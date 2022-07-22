# https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def getSum(node):
            if not node:
                return 0
            
            cur_sum = node.val + getSum(node.left) + getSum(node.right)
            subsums[cur_sum] += 1
            return cur_sum
            
        subsums = defaultdict(int)
        getSum(root)
        
        freqs = defaultdict(list)
        for key, val in subsums.items():
            freqs[val].append(key)
            
        return freqs[max(freqs.keys())]
    
