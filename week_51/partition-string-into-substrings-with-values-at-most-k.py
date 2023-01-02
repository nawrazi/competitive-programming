# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/description/

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        cur = 0
        partitions = 1
        
        for num in s:
            if cur * 10 + int(num) <= k:
                cur = cur * 10 + int(num)
            elif int(num) > k:
                return -1
            else:
                cur = int(num)
                partitions += 1
                
        return partitions
    
