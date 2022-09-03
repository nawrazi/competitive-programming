# https://codeforces.com/gym/397282/problem/A

def solve():
    a = input()
    b = input()
    if len(a) != len(b):
        print(max(len(a), len(b)))
        return

    for i in range(len(a)):
        if a[i] != b[i]:
            print(len(a))
            return
    
    print(-1)

solve()
