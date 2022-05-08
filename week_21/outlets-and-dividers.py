# https://codeforces.com/gym/380981/problem/A

def solve(dividers, students):
    dividers.sort(reverse = True)
    outlets = 2
    used = 0
    
    for i in range(len(dividers)):
        if outlets >= students:
            break
        used += 1
        outlets += dividers[i] - 1
 
    ans = used if outlets >= students else -1
    print(ans)
 
 
t = int(input())
for _ in range(t):
    s, o = [int(i) for i in input().split()]
    dividers = [int(i) for i in input().split()]
    solve(dividers, s)
