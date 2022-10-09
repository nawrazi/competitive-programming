# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(idx):
            cur = ''
            while idx < len(s) and s[idx] != ']':
                if s[idx].isnumeric():
                    num = ''
                    while s[idx].isnumeric():
                        num += s[idx]
                        idx += 1
                    nex_str, nex_idx = decode(idx + 1)
                    cur += int(num) * nex_str
                    idx = nex_idx
                else:
                    cur += s[idx]
                idx += 1
                
            return cur, idx
                
        return decode(0)[0]
    
