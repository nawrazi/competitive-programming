# https://leetcode.com/problems/largest-number/submissions/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(reverse=True)
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if int(nums[j]+nums[i]) > int(nums[i]+nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]

        result = ''.join([x for l in nums for x in l])

        return result if int(result)!=0 else "0"
