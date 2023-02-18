for _ in range(int(input())):
    n = int(input())
    line = input()
    
    value = 0
    for i in range(n):
        if line[i] == 'L':
            value += i
        else:
            value += n - i - 1
            
    gain = []
    for i in range(n):
        if line[i] == 'L':
            old = i
            new = n - i - 1
            if new > old:
                gain.append(new - old)
        else:
            old = n - i - 1
            new = i
            if new > old:
                gain.append(new - old)
    gain.sort()
    
    res = []
    for i in range(n):
        if gain:
            value += gain.pop()
        res.append(value)
        
    print(*res)
    
