# https://codeforces.com/gym/395482/problem/B

from collections import deque

def solve():
    t = int(input())
    for _ in range(t):
        n = input()
        candies = deque(int(i) for i in input().split())
        best = 0
        eaten = 0
        net = 0
        turn = 1
        while candies:
            # print(candies)
            if turn:
                while candies and net < 0:
                    # print(candies)
                    # print('xx')
                    net += candies.pop()
                    eaten += 1
            else:
                while candies and net > 0:
                    # print('yy')
                    # print(candies)
                    net -= candies.popleft()
                    eaten += 1
            if net == 0:
                best = eaten
                if candies and turn:
                    net += candies.pop()
                    eaten += 1
                    # print('zz')
                elif candies:
                    net -= candies.popleft()
                    # print('ww')
                    eaten += 1

            turn ^= 1

        print(best)

solve()
