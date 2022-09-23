# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for _ in range(n)]
        
        num = 2
        while num * num <= n - 1:
            if prime[num]:
                for mult in range(num * num, n, num):
                    prime[mult] = False
            num += 1
                
        return prime[2:].count(True)
    
