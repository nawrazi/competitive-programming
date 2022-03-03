# https://leetcode.com/problems/top-k-frequent-words/submissions/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}

        for word in words:
            if word in d:
                d[word]+=1
                continue
            d[word]=1

        tuples = []
        for word in words:
            tuples.append((d[word]*-1,word))

        tuples = list(set(tuples))

        heapq.heapify(tuples)
        final=[]

        for i in range(k):
            _,item = heapq.heappop(tuples)
            final.append(item)

        return final
