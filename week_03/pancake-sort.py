# https://leetcode.com/problems/pancake-sorting/submissions/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ks = []
        k = len(arr)
        while k>1:
            m = arr.index(max(arr[:k]))
            arr = arr[m::-1] + arr[m+1:]
            arr = arr[k-1::-1] + arr[k:]

            ks.append(m+1) if m>0 else None
            ks.append(k) if k>0 else None

            k-=1

        return ks
