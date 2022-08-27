# https://codeforces.com/gym/396349/problem/E

t = int(input())
for _ in range(t):
    n = input()
    levels = [int(i) for i in input().split()]
    my_turn = 0
    pos = 0
    skips = 0
    
    while pos < len(levels):
        if my_turn:
            pos -= 1
            pass
        else:
            skips += levels[pos]
            if pos < len(levels) - 1 and levels[pos + 1] == 0:
                pass
            elif pos < len(levels) - 2 and levels[pos + 2] == 1:
                pos += 2
            else:
                pos += 1
        pos += 1
        my_turn ^= 1
        
    print(skips)
