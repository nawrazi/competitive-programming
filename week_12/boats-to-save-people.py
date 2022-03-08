# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
                
            boats += 1

        return boats
