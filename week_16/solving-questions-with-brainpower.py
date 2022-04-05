# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def pick_or_skip(idx):
            if idx >= len(questions):
                return 0

            pick = questions[idx][0] + pick_or_skip(idx + questions[idx][1] + 1)
            skip = pick_or_skip(idx + 1)

            return max(pick, skip)

        return pick_or_skip(0)
