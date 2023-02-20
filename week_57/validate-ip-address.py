# https://leetcode.com/problems/validate-ip-address/description/

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validIPv4Item(item):
            if not item.isdigit() or (item[0] == '0' and len(item) > 1):
                return False
            return 0 <= int(item) <= 255
        
        def validIPv6Item(item):
            if not 1 <= len(item) <= 4:
                return False
            for c in item:
                if c.isdigit() or ord('a') <= ord(c) <= ord('f') or ord('A') <= ord(c) <= ord('F'):
                    continue
                return False
            return True
        
        def validIPv4(ip):
            for item in ip.split('.'):
                if not validIPv4Item(item):
                    return False
            return True
        
        def validIPv6(ip):
            for item in ip.split(':'):
                if not validIPv6Item(item):
                    return False
            return True
        
        if len(queryIP.split('.')) == 4:
            return 'IPv4' if validIPv4(queryIP) else 'Neither'
        
        if len(queryIP.split(':')) == 8:
            return 'IPv6' if validIPv6(queryIP) else 'Neither'
        
        return 'Neither'
    
