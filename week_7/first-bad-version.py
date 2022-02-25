# https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        best = n

        while start<=end:
            mid = (start+end)//2

            if isBadVersion(mid):
                best = mid
                end = mid-1
            else:
                start = mid+1

        return best
