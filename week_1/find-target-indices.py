# https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        indices=[]
        for i in range(n):
            if nums[i]==target:
                indices.append(i)

        return indices
