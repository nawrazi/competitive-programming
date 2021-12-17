# https://leetcode.com/problems/reduce-array-size-to-the-half/submissions/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = [1]
        n = len(arr)
        arr.sort()

        for i in range(n-1):
            if arr[i]==arr[i+1]:
                l[-1]+=1
            else:
                l.append(1)

        h=n//2
        l.sort()
        counter=0
        while n>h:
            n-=l.pop()
            counter+=1

        return counter
