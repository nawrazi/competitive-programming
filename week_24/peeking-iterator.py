# https://leetcode.com/problems/peeking-iterator/

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = deque([])

    def peek(self):
        if not self.cache:
            self.cache.append(self.iterator.next())
        return self.cache[0]
        
    def next(self):
        if self.cache:
            return self.cache.popleft()
        return self.iterator.next()
        
    def hasNext(self):
        return bool(self.cache) or self.iterator.hasNext()
      
