# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        data = {}
        for i in range(len(nums[0])):
            trim = len(nums[0]) - i -1
            data[i+1] = sorted([(int(num[trim:]), idx) for idx, num in enumerate(nums)])
        
        return [data[trim][k-1][1] for k, trim in queries]
    
