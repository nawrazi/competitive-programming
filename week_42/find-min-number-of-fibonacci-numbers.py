# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1, 1]
        while fibonacci[-1] < k:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            
        nums = 0
        cur = len(fibonacci) - 1
        while cur > 0:
            if k >= fibonacci[cur]:
                nums += k // fibonacci[cur]
                k -= fibonacci[cur]
            cur -= 1
            
        return nums
    
