# https://leetcode.com/problems/corporate-flight-bookings/description/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0 for _ in range(n + 2)]
        for first, last, seats in bookings:
            flights[first] += seats
            flights[last + 1] -= seats
            
        flights = list(accumulate(flights))
        return flights[1:-1]
    
