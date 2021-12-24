# https://www.hackerrank.com/challenges/equal-stacks/problem

def equalStacks(h1, h2, h3):
    l1, l2, l3 = sum(h1), sum(h2), sum(h3)

    while not (l1==l2 and l2==l3):
        maxim = max(l1,l2,l3)

        if l1 == maxim:
            l1 -= h1.pop(0)
        elif l2 == maxim:
            l2 -= h2.pop(0)
        elif l3 == maxim:
            l3 -= h3.pop(0)

    return l1
