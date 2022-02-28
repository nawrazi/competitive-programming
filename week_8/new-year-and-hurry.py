def timeTaken(n):
    return (5*n*(n+1))//2

def calculate(problems, time_rem):
    start, end = 0, problems
    best = 0

    while start<=end:
        mid = (start+end)//2

        if timeTaken(mid)<=time_rem:
            best = mid
            start = mid+1
        else:
            end = mid-1

    print(best)


problems, trip_time = [int(n) for n in input().split()]

time_rem = 240 - trip_time

calculate(problems, time_rem)
