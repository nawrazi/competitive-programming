# https://leetcode.com/problems/maximum-swap/description/

class Solution:
    def maximumSwap(self, num: int) -> int:
        max_num = num
        num = list(str(num))
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                cur_num = int(''.join(num))
                max_num = max(max_num, cur_num)
                num[i], num[j] = num[j], num[i]
                
        return max_num
    
