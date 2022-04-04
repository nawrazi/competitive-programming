# https://www.hackerrank.com/contests/a2sv-3-contest-4/challenges/reduced-string

def superReducedString(s, changed=False):
    i, j = 0, 1
    l = list(s)

    while j < len(s):
        if l[j] == l[i]:
            l.pop(i)
            l.pop(i)
            changed = True
            n-=2
        i+=1
        j+=1

    if changed:
        return superReducedString(''.join(l), False)

    if l == []:
        return 'Empty String'

    return ''.join(l)
