# https://leetcode.com/problems/daily-temperatures/submissions/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        mono_stack = []
        waits = [0]*n

        for i in range(n):
            if not mono_stack:
                mono_stack.append((temperatures[i],i))
                continue

            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                print(temperatures[i])
                val, index = mono_stack.pop()
                waits[index] = i - index

            mono_stack.append((temperatures[i],i))

        return waits
