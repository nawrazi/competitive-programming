# https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 1 if isBadVersion(1) else 2

        current, best = n//2, n

        while best!=current:
            if isBadVersion(current):
                best = current
                current = current//2
            else:
                current = current + current//2

        return best
