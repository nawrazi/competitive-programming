# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        evens, odds = defaultdict(int), defaultdict(int)

        for i, num in enumerate(nums):
            if i % 2 == 0:
                evens[num] += 1
            else:
                odds[num] += 1

        oddList = sorted([(n, odds[n]) for n in odds] + [(99,0)], key = lambda x : x[1])
        evenList = sorted([(n, evens[n]) for n in evens] + [(99,0)], key = lambda x : x[1])

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
