# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        forward = [1]

        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                forward.append(forward[-1] + 1)
            else:
                forward.append(1)

        total = []
        last = 1
        for i in range(len(security) - 1, -1, -1):
            if security[i] >= security[i-1]:
                current = last + 1
            else:
                current = 1

            if last > time and forward[i] > time:
                total.append(i)

            last = current

        return total
