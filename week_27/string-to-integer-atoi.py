# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        nums = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '6': 6, '7': 7, '8': 8, '9': 9, '5': 5
        }
        signs = {'-': -1, '+': 1}

        sign = 1
        digits = []
        for i, c in enumerate(s):
            if c in nums:
                digits.append(nums[c])
            elif c in signs and i == 0:
                sign *= signs[c]
            else:
                break

        ans = 0
        for i, digit in enumerate(digits):
            ans += digit * (10 ** (len(digits) - i - 1))

        if ans > (2 ** 31) - 1:
            return (2 ** 31) - 1 if sign == 1 else -(2 ** 31)

        return ans * sign
