# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        last_num, moves = -1, 0

        for cur_num in nums:
            if cur_num <= last_num:
                diff = last_num - cur_num + 1
                cur_num += diff
                moves += diff
            last_num = cur_num

        return moves
