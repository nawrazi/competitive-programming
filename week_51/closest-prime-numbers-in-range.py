# https://leetcode.com/problems/closest-prime-numbers-in-range/description/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getPrimes(start, end):
            prime = [True for _ in range(end)]
            
            num = 2
            while num * num <= end - 1:
                if prime[num]:
                    for mult in range(num * num, end, num):
                        prime[mult] = False
                num += 1
                
            return [i for i, p in enumerate(prime[start:], start) if p]
        
        primes = getPrimes(max(2, left), right + 1)
        closest = [0, inf]
        
        for i in range(1, len(primes)):
            closest = min(closest, [primes[i-1], primes[i]], key=lambda x: x[1] - x[0])
            
        return closest if closest[0] != 0 else [-1, -1]
    
