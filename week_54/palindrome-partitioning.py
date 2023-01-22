# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
                
            return True
        
        partitions = []
        cur = []
        
        def backtrack(idx):
            if idx >= len(s):
                partitions.append(cur[:])
                return
            
            for nex in range(idx, len(s)):
                if isPalindrome(idx, nex):
                    cur.append(s[idx:nex + 1])
                    backtrack(nex + 1)
                    cur.pop()
        
        backtrack(0)
        return partitions
    
