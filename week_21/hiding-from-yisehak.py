# https://codeforces.com/gym/380981/problem/B

def solve2(students):
    hidden = 0
    cur_tallest = 0
 
    for i in range(len(students) - 1, -1, -1):
        cur_tallest = max(students[i], cur_tallest)
 
        if students[i] < cur_tallest:
            hidden += 1
 
    print(hidden)
 
 
c = int(input())
for _ in range(c):
    n = int(input())
    students = [int(i) for i in input().split()]
    solve2(students)
    
