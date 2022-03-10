# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, stash: List[int]) -> int:
        def collect(house):
            if house >= len(stash) - 2:
                return stash[house]

            max_stash = 0
            for next_house in [house + 2, house + 3]:
                if next_house < len(stash):
                    if next_house in mem:
                        next_stash = mem[next_house]
                    else:
                        next_stash = collect(next_house)
                        mem[next_house] = next_stash

                    max_stash = max(max_stash, stash[house] + next_stash)

            return max_stash

        mem = {}

        return max(collect(0), collect(1)) if len(stash) > 1 else collect(0)
