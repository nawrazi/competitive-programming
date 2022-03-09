# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_points = 0

        for i in range(k):
            max_points += cardPoints[i]

        points = max_points
        for i in range(k):
            points -= cardPoints[k-1-i]
            points += cardPoints[~i]

            max_points = max(points, max_points)

        return max_points
