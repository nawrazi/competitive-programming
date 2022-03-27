# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        evens, odds = {}, {}

        for i, num in enumerate(nums):
            if i % 2 == 0:
                if num in evens:
                    evens[num] += 1
                else:
                    evens[num] = 1
            else:
                if num in odds:
                    odds[num] += 1
                else:
                    odds[num] = 1

        oddList = [(num, odds[num]) for num in odds] + [(99, 0)]
        evenList = [(num, evens[num]) for num in evens] + [(99, 0)]

        oddList.sort(key = lambda x : x[1])
        evenList.sort(key = lambda x : x[1])

        finalEven = evenList[-1][1]
        finalOdd = oddList[-1][1]

        if oddList[-1][0] == evenList[-1][0]:
            if evenList[-1][1] == evenList[-2][1]:
                finalEven = evenList[-2][1]
            elif oddList[-1][1] == oddList[-2][1]:
                finalOdd = oddList[-2][1]
            elif evenList[-2][1] > oddList[-2][1]:
                finalEven = evenList[-2][1]
            else:
                finalOdd = oddList[-2][1]

        return (ceil(len(nums) / 2) - finalEven) + (floor(len(nums) / 2) - finalOdd)
