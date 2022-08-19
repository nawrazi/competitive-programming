# https://codeforces.com/problemset/problem/604/B

def getBoxes(sizes, capacity):
    left, right = 0, len(sizes) - 1
    boxes = 0
    while left <= right:
        if left == right:
            left += 1
        elif sizes[right] + sizes[left] <= capacity:
            left += 1
            right -= 1
        else:
            right -= 1
        boxes += 1

    return boxes

def solve():
    _, k = [int(i) for i in input().split()]
    sizes = [int(i) for i in input().split()]

    if len(sizes) == 1:
        return sizes[0]

    start = max(sizes)
    end = sizes[-1] + sizes[-2]
    best = -1

    while start <= end:
        mid = (start + end) // 2
        boxes = getBoxes(sizes, mid)
        if boxes > k:
            start = mid + 1
        elif boxes < k:
            best = mid
            end = mid - 1
        else:
            best = mid
            end = mid - 1

    return best

print(solve())
