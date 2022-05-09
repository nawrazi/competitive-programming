# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]
        
        i = 0
        while i < min(len(v1), len(v2)):
            if v1[i] > v2[i]:
                return 1
            elif v2[i] > v1[i]:
                return -1
            i += 1
            
        if len(v1) > len(v2):
            return 1 if sum(v1[i:]) > 0 else 0
        else:
            return -1 if sum(v2[i:]) > 0 else 0
        
