# https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons, self.times = persons, times
        self.maxes = []
        self.findLeaders()

    def findLeaders(self):
        max_counts = (0,0)
        d = {}

        for i in range(len(self.persons)):
            if self.persons[i] in d:
                d[self.persons[i]]+=1
            else:
                d[self.persons[i]]=1

            if d[self.persons[i]]>=max_counts[1]:
                max_counts = (self.persons[i], d[self.persons[i]])

            self.maxes.append(max_counts[0])

    def q(self, t: int) -> int:
        start, end = 0, len(self.persons)-1
        best = 0

        while start<=end:
            mid = (start+end)//2

            if self.times[mid]<=t:
                best = mid
                start = mid+1
            else:
                end = mid-1

        return self.maxes[best]
