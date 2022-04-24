# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.total = sum(nums)
        self.sum_bef = {-1 : 0}
        self.sum_aft = {n : 0}

        for i in range(n):
            self.sum_bef[i] = self.sum_bef[i-1] + nums[i]
            self.sum_aft[n-i-1] = self.sum_aft[n-i] + nums[n-i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.total - self.sum_bef[left-1] - self.sum_aft[right+1]
