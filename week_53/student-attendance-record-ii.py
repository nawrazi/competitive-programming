# https://leetcode.com/problems/student-attendance-record-ii/description/

class Solution:
    def checkRecord(self, n: int) -> int:
        @cache
        def getRecords(day, absents, lates):
            if day == n:
                return 1
            
            ways = getRecords(day + 1, absents, 0)
            if absents < 1:
                ways += getRecords(day + 1, absents + 1, 0)
            if lates < 2:
                ways += getRecords(day + 1, absents, lates + 1)
                
            return ways % mod
        
        mod = pow(10, 9) + 7
        records = getRecords(0, 0, 0)
        getRecords.cache_clear()
        return records
    
