# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        mod = pow(10, 9) + 7
        prefix = [0 for _ in range(n + 1)]
        
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
            
        freq = [(prefix[0], 0)]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
            freq.append((prefix[i], i))
            
        nums.sort()
        freq.sort()
        
        optimal = [-1 for _ in range(n)]
        for _ in range(n):
            _, idx = freq.pop()
            num = nums.pop()
            optimal[idx] = num
            
        for i in range(1, n):
            optimal[i] += optimal[i - 1]
            
        optimal.insert(0, 0)
        total = 0
        
        for start, end in requests:
            total += optimal[end + 1] - optimal[start]
            
        return total % mod
    
