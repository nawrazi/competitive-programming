# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        letters = [letter for letter in palindrome]

        for i, _ in enumerate(letters):
            if letters[i] != 'a':
                temp = letters[i]
                letters[i] = 'a'
                if letters[i] != letters[~i]:
                    return ''.join(letters)
                else:
                    letters[i] = temp

        letters[-1] = 'b'

        return ''.join(letters) if letters[0] != letters[~0] else ''
