# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        half_len = (2**(n-1))//2
        bits = {'0':'1', '1':'0'}

        if n==2:
            return '0' if k==1 else '1'
        if n==1:
            return '0'

        if k>half_len:
            return bits[self.kthGrammar(n-1,k-half_len)]
        else:
            return self.kthGrammar(n-1,k)
