# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
                continue

            d[num]=1

        tuples = []
        for num in nums:
            tuples.append((d[num]*-1,num))

        tuples = list(set(tuples))

        heapq.heapify(tuples)
        final=[]

        for i in range(k):
            _,item = heapq.heappop(tuples)
            final.append(item)

        return final
