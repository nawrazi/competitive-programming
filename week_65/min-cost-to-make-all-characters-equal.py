# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution:
    def minimumCost(self, s: str) -> int:
        pre = []
        pre0 = -1
        pre1 = -1
        for i in range(len(s)//2):
            if i < len(s) - 1 and s[i] != s[i+1]:
                pre.append(min(len(s)-i, i+1))
            if s[i] == '1':
                pre1 = len(pre) - 1
            else:
                pre0 = len(pre) - 1
        
        post = []
        post0 = -1
        post1 = -1
        for i in range(len(s)-1, len(s)//2-1, -1):
            if i > 0. and s[i] != s[i-1]:
                post.append(min(len(s)-i, i+1))
            if s[i] == '1':
                post1 = len(post) - 1
            else:
                post0 = len(post) - 1
        
        zero = sum(pre[:pre0+1]) + sum(post[:post0+1])
        one = sum(pre[:pre1+1]) + sum(post[:post1+1])
        
        return min(zero, one)
    
