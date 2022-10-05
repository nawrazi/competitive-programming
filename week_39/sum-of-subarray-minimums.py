# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        valley = [[0, 0] for _ in arr]
        
        stack = []
        for i, num in enumerate(arr + [0]):
            cur = [i, 0]
            while stack and num < arr[stack[-1][0]]:
                idx, val = stack.pop()
                valley[idx][0] += val
                cur[1] += 1 + val
                
            stack.append(cur)
            
        stack = []
        for i, num in enumerate(reversed([0] + arr)):
            cur = [len(arr) - i - 1, 0]
            while stack and num <= arr[stack[-1][0]]:
                idx, val = stack.pop()
                valley[idx][1] += val
                cur[1] += 1 + val
                
            stack.append(cur)
            
        return sum(arr[i] * (l + 1) * (r + 1) for i, (l, r) in enumerate(valley)) % mod
    
