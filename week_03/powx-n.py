# https://leetcode.com/problems/powx-n/submissions/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1

        if n==-1: return 1/x

        if n==1: return x

        rem = x if n%2!=0 else 1

        return self.myPow(x*x,n//2) * rem
