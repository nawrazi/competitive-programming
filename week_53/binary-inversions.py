# https://codeforces.com/gym/421762/problem/B

def inversions(arr):
    ones = 0
    inv = 0
    for a in arr:
        if a == 1:
            ones += 1
        else:
            inv += ones
    return inv

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    most = inversions(arr)

    # first 0 to 1
    index = -1
    for i in range(n):
        if arr[i] == 0:
            index = i
            break

    if index != -1:
        arr[index] = 1
        most = max(most, inversions(arr))
        arr[index] = 0

    # last 1 to 0
    index = -1
    for i in range(n):
        if arr[i] == 1:
            index = i

    if index != -1:
        arr[index] = 0
        most = max(most, inversions(arr))
        arr[index] = 1

    print(most)
    
