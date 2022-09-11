# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = sorted([(-f, n) for n, f in Counter(nums).items() if n % 2 == 0])
        return counts[0][1] if counts else -1
    
