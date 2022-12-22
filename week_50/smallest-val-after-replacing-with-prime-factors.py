# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/

class Solution:
    def smallestValue(self, n: int) -> int:
        def getPrimes(n):
            prime = [True for _ in range(n)]
            
            num = 2
            while num * num <= n - 1:
                if prime[num]:
                    for mult in range(num * num, n, num):
                        prime[mult] = False
                num += 1
                
            return [i + 2 for i, p in enumerate(prime[2:]) if p]
        
        primes = getPrimes(n + 1)
        last = set(primes)
        
        while n not in last:
            prev, new = n, 0
            for prime in primes:
                while n % prime == 0:
                    new += prime
                    n //= prime
            n = new
            if new == prev:
                break
                
        return n
    
