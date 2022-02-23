def cookies(k, A):
    n = len(A)
    heap = A
    heapq.heapify(heap)
    count = 0

    while heap[0]<k:
        if n==1:
            return -1

        least = heapq.heappop(heap)
        second = heapq.heappop(heap)

        combo = least + (2*second)

        heapq.heappush(heap,combo)

        count+=1
        n-=1

    return count
