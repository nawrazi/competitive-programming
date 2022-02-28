import heapq

def calculate(sushis):
    consecs = []
    counter = 1
    for i in range(1, len(sushis)):
        if sushis[i]==sushis[i-1]:
            counter+=1
        else:
            consecs.append(counter)
            counter=1
    consecs.append(counter)

    best = 0
    i = 1
    while i < len(consecs):
        if min(consecs[i],consecs[i-1])>best:
            best = min(consecs[i],consecs[i-1])
        i+=1

    print(2*best)


n = int(input())
sushis = [int(n) for n in input().split()]

calculate(sushis)
