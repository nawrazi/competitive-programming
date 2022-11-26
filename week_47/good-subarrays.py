# https://codeforces.com/gym/412541/problem/B

for _ in range(int(input())):
    input()
    arr = [0] + [int(n) for n in list(input())]
    diffs = {0: 1}
    good = 0
    
    pre = 0
    for i, a in enumerate(arr[1:], 1):
        pre += a
        cur = diffs.get(pre - i, 0)
        good += cur
        diffs[pre - i] = cur + 1
        
    print(good)
    
