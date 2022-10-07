# https://binarysearch.com/room/Bytesize-pointers-3sz2jB5VEg?questionsetIndex=2

class Solution:
    def solve(self, n):
        if n == 0:
            return []

        loners = ['0', '1', '8']
        nums = ['0', '1', '6', '8', '9']
        pair = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        halves = []
        cur = []

        def backtrack():
            if len(cur) == n // 2:
                halves.append(cur[:])
                return

            for num in nums:
                cur.append(num)
                backtrack()
                cur.pop()

        backtrack()
        new_halves = []
        if n % 2 == 1:
            for h in halves:
                for l in loners:
                    new_halves.append(h + [l])
        else:
            new_halves = halves[:]

        for h in new_halves:
            for i in range((n // 2) - 1, -1, -1):
                h.append(pair[h[i]])

        ans = []
        for f in new_halves:
            if set(f) != {'0'} and f[0] != '0':
                ans.append(''.join(f))
        
        if n == 1:
            ans.append('0')
            
        return sorted(ans)
    
