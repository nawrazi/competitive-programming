# https://leetcode.com/contest/weekly-contest-120/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])
