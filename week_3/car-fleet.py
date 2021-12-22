# https://leetcode.com/problems/car-fleet/submissions/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = sorted([(pos, spd) for pos, spd in zip(position,speed)])

        times = []
        n = len(position)

        for i in range(n):
            current_time = (target-tuples[i][0]) / tuples[i][1]

            if len(times)==0:
                times.append(current_time)
                continue

            while times and current_time >= times[-1]:
                times.pop()

            times.append(current_time)

        return len(times)
