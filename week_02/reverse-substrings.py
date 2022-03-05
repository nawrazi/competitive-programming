# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        d = {'(':')', ')':'('}
        s = list(s)
        i=0
        while i < len(s):
            if s[i] in d.keys():
                j=i+1
                c=0
                while j < len(s):
                    if c>0:
                        break

                    if s[j] == s[i]:
                        c-=1
                    elif s[j] == d[s[i]]:
                        c+=1
                    j+=1

                s[i+1:j] = s[i+1:j][::-1]
                s.pop(i)
                s.pop(i)
                i-=1

            i+=1

        return ''.join(s)
