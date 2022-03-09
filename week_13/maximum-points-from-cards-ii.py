# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        options = cardPoints[~k+1:] + cardPoints[:k]

        cur_points = sum(cardPoints[~k+1:])
        max_points = cur_points

        i, j = 0, k
        while j < 2*k:
            cur_points -= options[i]
            cur_points += options[j]

            max_points = max(cur_points, max_points)

            i += 1
            j += 1

        return max_points
