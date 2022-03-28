# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        locked_openers, unlocked_pars = [], []

        for i, par in enumerate(s):
            if locked[i] == '0':
                unlocked_pars.append(i)
            elif par == '(':
                locked_openers.append(i)
            else:
                closable = locked_openers or unlocked_pars
                if closable:
                    closable.pop()
                else:
                    return False

        while unlocked_pars and locked_openers and unlocked_pars[-1] > locked_openers[-1]:
            unlocked_pars.pop()
            locked_openers.pop()

        return not locked_openers
