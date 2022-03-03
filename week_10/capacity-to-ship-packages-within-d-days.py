# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def findDays(capacity):
            sub_sum = 0
            total_days = 0

            for weight in weights:
                if sub_sum + weight <= capacity:
                    sub_sum += weight
                else:
                    sub_sum = weight
                    total_days += 1

            return total_days+1 if sub_sum else total_days


        max_weight = max(weights)
        start, end = max_weight, max_weight * len(weights)
        best = max_weight

        while start<=end:
            mid = (start+end)//2

            if findDays(mid) <= days:
                best = mid
                end = mid - 1
            else:
                start = mid + 1

        return best
