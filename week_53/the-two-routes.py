# https://codeforces.com/gym/421762/problem/D

from collections import deque

t, r = [int(i) for i in input().split()]
rails = set()

for _ in range(r):
    rails.add(tuple(int(i) for i in input().split()))
    
road = [set() for _ in range(t + 1)]
rail = [set() for _ in range(t + 1)]

for n1 in range(1, t + 1):
    for n2 in range(n1 + 1, t + 1):
        if (n1, n2) in rails or (n2, n1) in rails:
            rail[n1].add(n2)
            rail[n2].add(n1)
        else:
            road[n1].add(n2)
            road[n2].add(n1)
            
def trainTime():
    q = deque([(1, 0)])
    seen = {1}
    
    while q:
        node, time = q.popleft()
        
        if node == t:
            return time
        
        for ngh in rail[node]:
            if ngh in seen:
                continue
                
            if time + 1 != opp[ngh] or ngh == t:
                seen.add(ngh)
                q.append((ngh, time + 1))
                opp[ngh] = time + 1
                
    return float('inf')

def busTime():
    q = deque([(1, 0)])
    seen = {1}
    
    while q:
        node, time = q.popleft()
        
        if node == t:
            return time
        
        for ngh in road[node]:
            if ngh in seen:
                continue
                
            if time + 1 != opp[ngh] or ngh == t:
                seen.add(ngh)
                q.append((ngh, time + 1))
                opp[ngh] = time + 1
                
    return float('inf')

opp = [-1 for _ in range(t + 1)]
bus = busTime()
train = trainTime()
bt = (bus, train)

opp = [-1 for _ in range(t + 1)]
train = trainTime()
bus = busTime()
tb = (train, bus)

ans = min(max(bt), max(tb))
print(ans if ans != float('inf') else -1)
