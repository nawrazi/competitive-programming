# https://binarysearch.com/room/Bytesize-pointers-3sz2jB5VEg?questionsetIndex=3

class Solution:
    def solve(self, ip):
        ips = []
        cur = []
        
        def getIps(idx):
            if len(cur) == 4:
                if idx >= len(ip):
                    ips.append('.'.join(cur))
                else:
                    return
                
            if idx >= len(ip):
                return
            
            cur.append(ip[idx])
            getIps(idx + 1)
            cur.pop()
            
            if ip[idx] == '0':
                return
            
            if idx < len(ip) - 1:
                cur.append(ip[idx:idx+2])
                getIps(idx + 2)
                cur.pop()
                
            if idx < len(ip) - 2 and int(ip[idx:idx+3]) <= 255:
                cur.append(ip[idx:idx+3])
                getIps(idx + 3)
                cur.pop()
                
        getIps(0)
        return ips
    
