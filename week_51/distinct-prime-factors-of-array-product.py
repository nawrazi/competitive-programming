# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def getPrimes(n):
            prime = [True for _ in range(n)]
            
            num = 2
            while num * num <= n - 1:
                if prime[num]:
                    for mult in range(num * num, n, num):
                        prime[mult] = False
                num += 1
                
            return [i for i, p in enumerate(prime[2:], 2) if p]
        
        primes = getPrimes(1000)
        factors = set()
        
        for num in nums:
            for prime in primes:
                if num % prime == 0:
                    num //= prime
                    factors.add(prime)
                if prime > num:
                    break
                    
        return len(factors)
    
