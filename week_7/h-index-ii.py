# https://leetcode.com/problems/h-index-ii/submissions/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1
        best = -1

        while left<=right:
            mid = (left+right)//2

            if (len(citations)-mid) <= citations[mid]:
                best = mid
                right = mid-1

            else:
                left = mid+1

        return len(citations)-best if best!=-1 else 0
