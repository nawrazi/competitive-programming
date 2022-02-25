# https://leetcode.com/problems/find-the-duplicate-number/submissions/

class Solution:
    def count(self, nums, mid, end):
        total = 0
        for num in nums:
            if num>mid and num<=end:
                total+=1
        return total

    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, max(nums)

        while start<=end:
            mid = (start+end)//2
            exp_after_mid = end-mid
            act_after_mid = self.count(nums,mid,end)
            if start==end:
                return mid
            if exp_after_mid >= act_after_mid:
                end = mid
            else:
                start = mid+1

        return mid
