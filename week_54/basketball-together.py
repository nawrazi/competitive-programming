# https://codeforces.com/gym/421768/problem/B

n, d = [int(i) for i in input().split()]
power = sorted(int(i) for i in input().split())

rep = n - 1
fol = 0
wins = 0

while fol <= rep:
    need = d // power[rep]
    fol += need
    
    if fol <= rep and (need + 1) * power[rep] > d:
        wins += 1
        
    rep -= 1
    
print(wins)
