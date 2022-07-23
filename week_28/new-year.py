points = [int(i) for i in input().split()]

min_dist = float('inf')
for ave in range(min(points), max(points) + 1):
    dist = abs(points[0] - ave) + abs(points[1] - ave) + abs(points[2] - ave)
    min_dist = min(min_dist, dist)

print(min_dist)