# https://codeforces.com/contest/2/problem/A

from collections import defaultdict

r = int(input())
rounds = [input().split() for _ in range(r)]
scores = defaultdict(int)

for name, points in rounds:
    scores[name] += int(points)

max_pts = max(scores.values())
winners = {n for n, p in scores.items() if p == max_pts}
scores.clear()

for name, points in rounds:
    scores[name] += int(points)
    if scores[name] >= max_pts and name in winners:
        print(name)
        break
    
