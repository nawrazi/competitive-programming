# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        
        for num in nums:
            node = trie
            for i in range(31, -1, -1):
                bit = 1 if num & 1 << i else 0
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
                
        def xor(num):
            node = trie
            ans = 0
            for i in range(31, -1, -1):
                bit = 1 if num & 1 << i else 0
                if 1 - bit in node:
                    node = node[1 - bit]
                    ans |= 1 << i
                else:
                    node = node[bit]
                    
            return ans
        
        best = 0
        for num in nums:
            best = max(best, xor(num))
            
        return best
    
