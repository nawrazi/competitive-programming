_, fence = [int(i) for i in input().split()]
heights = [int(i) for i in input().split()]

width = 0
for h in heights:
    if h <= fence:
        width += 1
    else:
        width += 2

print(width)