# https://codeforces.com/contest/1676/problem/E

class Solution:
    def __init__(self, candies):
        self.candies = sorted(candies, reverse = True)
        self.prefixSum()

    def prefixSum(self):
        for i in range(1, len(self.candies)):
            self.candies[i] += self.candies[i-1]

    def search(self, cal):
        start, end = 0, len(self.candies) - 1
        best = -2

        while start <= end:
            mid = (start + end) // 2

            if self.candies[mid] >= cal:
                best = mid
                end = mid - 1
            else:
                start = mid + 1

        print(best + 1)


t = int(input())
for _ in range(t):
    n, q = [int(i) for i in input().split()]
    candies = [int(i) for i in input().split()]
    sol = Solution(candies)
    for __ in range(q):
        cal = int(input())
        sol.search(cal)
        
