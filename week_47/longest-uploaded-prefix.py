# https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix:

    def __init__(self, n: int):
        self.prefix = 0
        self.pending = set()
        
    def upload(self, video: int) -> None:
        self.pending.add(video)
        
    def longest(self) -> int:
        while self.prefix + 1 in self.pending:
            self.prefix += 1
            
        return self.prefix
    
