# https://leetcode.com/contest/weekly-contest-120/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        prepend = [float(-inf)] if arr[0] >= arr[1] else [float(inf)]
        postpend = [float(-inf)] if arr[-1] >= arr[-2] else [float(inf)]
        arr = prepend + arr + postpend

        longest = 0
        turbulence = 0
        here = False

        i = 1
        while i < len(arr) - 1:
            if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
                turbulence += 1
                here = True
            else:
                if here:
                    turbulence += 1
                longest = max(longest, turbulence)
                turbulence = 1
                here = False

            i += 1

        return max(longest, turbulence)
