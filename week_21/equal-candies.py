# https://codeforces.com/contest/1676/problem/B

def solve(candies):
    m = min(candies)
    eat = 0
    for candy in candies:
        eat += candy - m

    print(eat)

t = int(input())
for _ in range(t):
    n = input()
    candies = [int(i) for i in input().split()]
    solve(candies)
    
