# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
                continue

            dict[num]=1

        keys = list(dict.keys())
        vals = list(dict.values())

        final = []
        for i in range(k):
            ind = vals.index(max(vals))
            vals.pop(ind)
            final.append(keys.pop(ind))

        return final
