# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        ones = 0
        twos = 0
        for num in nums:
            if num==0:
                zeros+=1
            elif num==1:
                ones+=1
            elif num==2:
                twos+=1
        nums.clear()
        for i in range(zeros):
            nums.append(0)
        for i in range(ones):
            nums.append(1)
        for i in range(twos):
            nums.append(2)
