# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_seen = {}
        picked, max_picked = 0, 0

        for i, fruit in enumerate(fruits):
            if len(last_seen) < 2:
                last_seen[fruit] = i
                picked += 1
                continue

            most_recent = max(last_seen.values())

            if fruits[i] in last_seen:
                if last_seen[fruit] != most_recent:
                    last_seen[fruit] = i

            else:
                max_picked = max(picked, max_picked)
                picked = i - most_recent

                last_seen = dict(filter(lambda x: x[1] == most_recent, last_seen.items()))
                last_seen[fruit] = i

            picked += 1

        return max(picked, max_picked)
