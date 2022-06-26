# https://codeforces.com/gym/387097/problem/A

s = input()
 
cur = s[0]
count = 0
flag = False
 
for p in s:
    if p == cur:
        count += 1
    else:
        cur = p
        count = 1
    if count >= 7:
        print('YES')
        flag = True
        break
 
if not flag:
    print('NO')
    
