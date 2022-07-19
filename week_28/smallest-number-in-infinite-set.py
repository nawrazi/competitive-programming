# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = deque([1000 - i for i in range(1000)])
        self.reserves = []
        self.popped = set()

    def popSmallest(self) -> int:
        result = self.inf_set.pop()
        self.popped.add(result)
        
        subs = []
        while self.reserves and self.reserves[0] < self.inf_set[-1]:
            subs.append(heappop(self.reserves))
        self.inf_set += reversed(subs)
        
        return result

    def addBack(self, num: int) -> None:
        if num not in self.popped:
            return
        if num < self.inf_set[-1]:
            self.inf_set.append(num)
            self.inf_set.popleft()
            self.popped.remove(num)
        else:
            heappush(self.reserves, num)
            
