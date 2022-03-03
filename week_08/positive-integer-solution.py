# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/submissions/

class Solution:
    def searchPair(self, customFunction, x, z):
        start, end = 1, 1000

        while start<=end:
            mid = (start+end)//2

            if customFunction.f(x,mid)>z:
                end = mid-1
            elif customFunction.f(x,mid)<z:
                start = mid+1
            else:
                return mid

        return -1


    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        pairs = []

        for x in range(1,1001):
            y = self.searchPair(customfunction,x,z)
            if y>0:
                pairs.append([x,y])

        return pairs
