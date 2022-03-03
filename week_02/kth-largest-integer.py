# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/submissions/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted([int(num) for num in nums])[len(nums)-k])
