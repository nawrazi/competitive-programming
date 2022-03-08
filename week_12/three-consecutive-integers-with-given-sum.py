# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        third = (num - 3) / 3
        if third % 1 == 0:
            third = int(third)
            return [third, third + 1, third + 2]
        else:
            return []
