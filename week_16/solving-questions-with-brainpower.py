# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def solve_or_skip(idx):
            if idx >= len(questions):
                return 0

            pick = questions[idx][0] + solve_or_skip(idx + questions[idx][1] + 1)
            skip = solve_or_skip(idx + 1)

            max_score = max(pick, skip)

            return max_score

        return solve_or_skip(0)
