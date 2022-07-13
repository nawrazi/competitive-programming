# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(cur, idx):
            ans.append(cur)
            for i in range(idx, len(nums)):
                search(cur + [nums[i]], i + 1)
            
        ans = []
        search([], 0)
        return ans
    
