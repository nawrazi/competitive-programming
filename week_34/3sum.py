# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        last = {n: i for i, n in enumerate(nums)}
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = -(nums[i] + nums[j])
                if diff in last and len({i, j, last[diff]}) == 3:
                    ans.add(tuple(sorted([nums[i], nums[j], diff])))
                    
        return ans
    
