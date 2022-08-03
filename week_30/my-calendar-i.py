# https://leetcode.com/problems/my-calendar-i/

from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        pos = bisect_left(self.events, [start, end])
        
        if pos > 0 and start < self.events[pos - 1][1]:
            return False
        
        if pos < len(self.events) and end > self.events[pos][0]:
            return False
        
        self.events.add([start, end])
        return True
    
