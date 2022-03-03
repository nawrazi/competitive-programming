# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/submissions/

class Solution:
    def findSum(self, nums, divisor):
        total = 0
        for num in nums:
            total+=(math.ceil(num/divisor))

        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        best = end

        while start<=end:
            mid = (start+end)//2
            total = self.findSum(nums,mid)

            if total<=threshold:
                best = mid
                end = mid-1
            else:
                start = mid+1

        return best
