# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t, b = len(num1) - 1, len(num2) - 1
        lines = []
        rem = 0
        
        while b >= 0:
            t = len(num1) - 1
            lines.append([])
            while t >= 0:
                prod = int(num2[b]) * int(num1[t])
                lines[-1].append((prod % 10) + rem)
                rem = prod // 10
                if lines[-1][-1] >= 10:
                    lines[-1][-1] %= 10
                    rem += 1
                t -= 1
            lines[-1].append(rem)
            lines[-1].reverse()
            rem = 0
            b -= 1
            
        ans_len = len(lines) + len(lines[0]) - 1
        ans = [0 for _ in range(ans_len)]
        rem = 0
        
        for i, line in enumerate(lines):
            for j in range(len(line) - 1, -1, -1):
                idx = j - i + ans_len - len(line)
                sm = ans[idx] + line[j]
                ans[idx] = (sm % 10) + rem
                rem = sm // 10
                if ans[idx] >= 10:
                    ans[idx] %= 10
                    rem += 1
                
        prod = ''.join([str(n) for n in ans]).lstrip('0')
        return prod if prod else '0'
      
