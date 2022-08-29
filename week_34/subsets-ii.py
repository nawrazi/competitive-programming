# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def search(cur, idx):
            ans.add(tuple(sorted(cur)))
            for i in range(idx, len(nums)):
                search(cur + [nums[i]], i + 1)
                
        ans = set()
        search([], 0)
        return ans
    
