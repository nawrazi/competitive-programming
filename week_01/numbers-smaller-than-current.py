# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vals = [0 for _ in range(n)]
        frequencies = [0 for _ in range(101)]

        for num in nums:
            frequencies[num]+=1

        for i in range(n):
            vals[i]=sum(frequencies[:nums[i]])

        return vals
