# https://leetcode.com/problems/h-index/submissions/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        total = len(citations)
        max_papers = 0

        for i in range(total-1, -1, -1):
            papers = total-i

            if citations[i]>=papers:
                max_papers = papers

        return max_papers
