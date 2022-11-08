# https://leetcode.com/problems/binary-watch/

class Solution:
    def generateTimes(self, turnedOn, hour, minute, times, hour_base, minute_base):
        bitCount = bin(hour)[2:].count('1') + bin(minute)[2:].count('1')
        
        if bitCount > turnedOn or hour > 11 or minute > 59:
            return
        if bitCount == turnedOn:
            times.add(f'{hour}:{self.timeString(minute)}')
            return
        
        for i in range(hour_base, 4):
            self.generateTimes(turnedOn, hour | (1 << i), minute, times, i + 1, minute_base)
            
        for i in range(minute_base, 6):
            self.generateTimes(turnedOn, hour, minute | (1 << i), times, hour_base, i + 1)
            
    def timeString(self, time):
        if time < 10:
            return f'0{time}'
        else:
            return str(time)
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = set()
        self.generateTimes(turnedOn, 0, 0, times, 0, 0)
            
        return times
    
