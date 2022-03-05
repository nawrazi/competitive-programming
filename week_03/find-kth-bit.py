# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def recur(self,n):
        if n==1:
            return '0'

        prev = self.recur(n-1)

        inverse = [('0' if bit=='1' else '1') for bit in prev]
        reverse = ''.join(inverse[::-1])

        return prev + '1' + reverse

    def findKthBit(self, n: int, k: int) -> str:
        return self.recur(n)[k-1]
