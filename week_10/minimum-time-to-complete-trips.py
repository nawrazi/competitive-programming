class Solution:
    def findTime(self, time, n):
        total = 0
        for i in range(len(time)):
            total += n//time[i]

        return total


    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 0, max(time)*totalTrips
        best = time[-1]

        while start<=end:
            mid = (start+end)//2
            total = self.findTime(time, mid)
            
            if total >= totalTrips:
                best = mid
                end = mid-1
            else:
                start = mid+1

        return best
