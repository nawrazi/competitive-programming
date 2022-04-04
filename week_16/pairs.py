# https://www.hackerrank.com/contests/a2sv-3-contest-4/challenges/pairs

def pairs(k, arr):
    arr.sort()
    count = 0
    i, j = 0, 0
    length = len(arr)

    while j<length:
        diff = arr[j] - arr[i]

        if diff==k:
            count+=1
            j+=1
        elif diff>k:
            i+=1
        elif diff<k:
            j+=1

    return count
