# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        cur = []
        
        def getIps(idx):
            if len(cur) == 4:
                if idx >= len(s):
                    ips.append('.'.join(cur))
                else:
                    return
                
            if idx >= len(s):
                return
            
            cur.append(s[idx])
            getIps(idx + 1)
            cur.pop()
            
            if s[idx] == '0':
                return
            
            if idx < len(s) - 1:
                cur.append(s[idx:idx+2])
                getIps(idx + 2)
                cur.pop()
                
            if idx < len(s) - 2 and int(s[idx:idx+3]) <= 255:
                cur.append(s[idx:idx+3])
                getIps(idx + 3)
                cur.pop()
                
        getIps(0)
        return ips
    
