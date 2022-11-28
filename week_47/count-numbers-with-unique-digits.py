# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def permutation(n, r):
            return factorial(n) // factorial(n - r)
        
        numbers = 1
        for digits in range(n):
            numbers += 9 * permutation(9, digits)
            
        return numbers
    
