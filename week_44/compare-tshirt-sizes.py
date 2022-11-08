# https://codeforces.com/contest/1741/problem/A

for _ in range(int(input())):
    a, b = input().split()
    val = {'S': -1, 'M': 0, 'L': 1}
    if a[-1] != b[-1]:
        if val[a[-1]] > val[b[-1]]:
            print('>')
        else:
            print('<')
    elif a[-1] == 'M':
        print('=')
    else:
        vala = len(a) * val[a[-1]]
        valb = len(b) * val[b[-1]]
        if vala > valb:
            print('>')
        elif vala < valb:
            print('<')
        else:
            print('=')
            
