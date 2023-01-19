# https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1, n + 1))
        
    def reserve(self) -> int:
        return heappop(self.seats)
    
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
        
