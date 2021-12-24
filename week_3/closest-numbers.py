# https://www.hackerrank.com/challenges/closest-numbers/problem

def closestNumbers(arr):
    arr.sort()
    n = len(arr)
    i = 0
    min_diff = []

    while i<n-1:
        diff = arr[i+1]-arr[i]

        if not min_diff:
            min_diff.append(arr[i])
            min_diff.append(arr[i+1])
            i+=1
            continue

        if diff < (min_diff[-1]-min_diff[-2]):
            min_diff = [arr[i], arr[i+1]]

        elif diff == (min_diff[-1]-min_diff[-2]):
            min_diff.append(arr[i])
            min_diff.append(arr[i+1])

        i+=1

    return min_diff
